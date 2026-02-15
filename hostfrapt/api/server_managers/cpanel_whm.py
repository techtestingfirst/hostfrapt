import frappe
import requests
import json
from frappe import _
from frappe.utils import cstr

class WHMManager:
    """WHM/cPanel API Manager for account provisioning"""
    
    def __init__(self, server_doc):
        """
        Initialize WHM Manager with server credentials
        
        Args:
            server_doc: Server DocType document
        """
        self.server = server_doc
        self.hostname = server_doc.hostname
        self.api_token = server_doc.get_password('api_password')  # Encrypted field
        self.base_url = f"https://{self.hostname}:2087"
        
    def _make_request(self, endpoint, params=None):
        """
        Make authenticated API request to WHM
        
        Args:
            endpoint: API endpoint (e.g., 'createacct')
            params: Dictionary of parameters
            
        Returns:
            dict: API response
        """
        headers = {
            'Authorization': f'WHM root:{self.api_token}'
        }
        
        url = f"{self.base_url}/json-api/{endpoint}"
        
        try:
            response = requests.get(
                url, 
                headers=headers, 
                params=params, 
                verify=True,  # Set to False for self-signed SSL (not recommended)
                timeout=30
            )
            response.raise_for_status()
            
            result = response.json()
            
            # Log the API call
            self._log_provisioning(endpoint, params, result, 'Success')
            
            return result
            
        except requests.exceptions.RequestException as e:
            error_msg = str(e)
            self._log_provisioning(endpoint, params, {'error': error_msg}, 'Failed')
            frappe.throw(_('WHM API Error: {0}').format(error_msg))
    
    def create_account(self, service_doc):
        """
        Create cPanel account
        
        Args:
            service_doc: Service DocType document
            
        Returns:
            dict: Creation result with username and password
        """
        product = frappe.get_doc('Hosting Product', service_doc.product)
        plan = frappe.get_doc('Hosting Plan', product.hosting_plan)
        
        # Generate username from domain (first 8 chars)
        domain = service_doc.domain_name
        username = domain.replace('.', '')[:8]
        
        # Generate secure random password
        password = frappe.generate_hash(length=16)
        
        params = {
            'username': username,
            'domain': domain,
            'password': password,
            'plan': plan.plan_name,  # Must match WHM package name
            'contactemail': service_doc.customer_email,
            'featurelist': 'default',
            'maxftp': plan.max_ftp_accounts or 'unlimited',
            'maxsql': plan.max_databases or 'unlimited',
            'maxpop': plan.max_email_accounts or 'unlimited',
            'maxlst': '0',
            'maxsub': plan.max_subdomains or 'unlimited',
            'maxpark': plan.max_parked_domains or 'unlimited',
            'maxaddon': plan.max_addon_domains or 'unlimited',
            'quota': plan.disk_quota_mb or 'unlimited',
            'bwlimit': plan.bandwidth_quota_mb or 'unlimited',
            'hasshell': 1 if plan.ssh_access else 0,
            'cgi': 1 if plan.cgi_access else 0,
        }
        
        # Add dedicated IP if specified
        if service_doc.dedicated_ip:
            params['ip'] = service_doc.dedicated_ip
        
        result = self._make_request('createacct', params)
        
        if result.get('metadata', {}).get('result') == 1:
            # Update service with credentials
            service_doc.username = username
            service_doc.set_password('password', password)
            service_doc.control_panel_url = f"https://{domain}:2083"
            service_doc.service_status = 'Active'
            service_doc.save(ignore_permissions=True)
            
            # Send welcome email
            self._send_welcome_email(service_doc)
            
            return {
                'success': True,
                'username': username,
                'password': password,
                'message': 'Account created successfully'
            }
        else:
            frappe.throw(_('Account creation failed: {0}').format(
                result.get('metadata', {}).get('reason', 'Unknown error')
            ))
    
    def suspend_account(self, service_doc):
        """
        Suspend cPanel account
        
        Args:
            service_doc: Service DocType document
        """
        params = {
            'user': service_doc.username,
            'reason': service_doc.suspension_reason or 'Non-payment'
        }
        
        result = self._make_request('suspendacct', params)
        
        if result.get('metadata', {}).get('result') == 1:
            service_doc.service_status = 'Suspended'
            service_doc.save(ignore_permissions=True)
            
            # Send suspension email
            self._send_suspension_email(service_doc)
            
            return {'success': True, 'message': 'Account suspended'}
        else:
            frappe.throw(_('Suspension failed'))
    
    def unsuspend_account(self, service_doc):
        """
        Unsuspend cPanel account
        
        Args:
            service_doc: Service DocType document
        """
        params = {'user': service_doc.username}
        
        result = self._make_request('unsuspendacct', params)
        
        if result.get('metadata', {}).get('result') == 1:
            service_doc.service_status = 'Active'
            service_doc.suspension_reason = ''
            service_doc.save(ignore_permissions=True)
            
            return {'success': True, 'message': 'Account unsuspended'}
        else:
            frappe.throw(_('Unsuspension failed'))
    
    def terminate_account(self, service_doc):
        """
        Terminate/delete cPanel account
        
        Args:
            service_doc: Service DocType document
        """
        params = {
            'user': service_doc.username,
            'keepdns': 0  # Set to 1 to keep DNS records
        }
        
        result = self._make_request('removeacct', params)
        
        if result.get('metadata', {}).get('result') == 1:
            service_doc.service_status = 'Terminated'
            service_doc.termination_date = frappe.utils.now()
            service_doc.save(ignore_permissions=True)
            
            return {'success': True, 'message': 'Account terminated'}
        else:
            frappe.throw(_('Termination failed'))
    
    def change_package(self, service_doc, new_plan_name):
        """
        Change cPanel account package
        
        Args:
            service_doc: Service DocType document
            new_plan_name: New WHM package name
        """
        params = {
            'user': service_doc.username,
            'pkg': new_plan_name
        }
        
        result = self._make_request('changepackage', params)
        
        if result.get('metadata', {}).get('result') == 1:
            return {'success': True, 'message': 'Package changed'}
        else:
            frappe.throw(_('Package change failed'))
    
    def change_password(self, service_doc, new_password):
        """
        Change cPanel account password
        
        Args:
            service_doc: Service DocType document
            new_password: New password
        """
        params = {
            'user': service_doc.username,
            'password': new_password
        }
        
        result = self._make_request('passwd', params)
        
        if result.get('metadata', {}).get('result') == 1:
            service_doc.set_password('password', new_password)
            service_doc.save(ignore_permissions=True)
            
            return {'success': True, 'message': 'Password changed'}
        else:
            frappe.throw(_('Password change failed'))
    
    def get_account_info(self, username):
        """
        Get account information
        
        Args:
            username: cPanel username
            
        Returns:
            dict: Account details
        """
        params = {'user': username}
        result = self._make_request('accountsummary', params)
        
        if result.get('data', {}).get('acct'):
            return result['data']['acct'][0]
        return None
    
    def get_disk_usage(self, username):
        """
        Get disk usage for account
        
        Args:
            username: cPanel username
            
        Returns:
            dict: Disk usage statistics
        """
        params = {'user': username}
        result = self._make_request('getdiskusage', params)
        
        if result.get('data'):
            return result['data']
        return None
    
    def get_bandwidth_usage(self, username):
        """
        Get bandwidth usage for account
        
        Args:
            username: cPanel username
            
        Returns:
            dict: Bandwidth usage statistics
        """
        params = {'user': username, 'searchtype': 'user'}
        result = self._make_request('showbw', params)
        
        if result.get('data'):
            return result['data']
        return None
    
    def list_packages(self):
        """
        List all WHM packages
        
        Returns:
            list: Available packages
        """
        result = self._make_request('listpkgs')
        
        if result.get('data', {}).get('pkg'):
            return result['data']['pkg']
        return []
    
    def _log_provisioning(self, action, request_data, response_data, status):
        """
        Log provisioning action for debugging
        
        Args:
            action: API action performed
            request_data: Request parameters
            response_data: API response
            status: Success/Failed
        """
        try:
            log = frappe.get_doc({
                'doctype': 'Provisioning Log',
                'server': self.server.name,
                'action': action,
                'request_payload': json.dumps(request_data, indent=2),
                'response': json.dumps(response_data, indent=2),
                'status': status,
                'timestamp': frappe.utils.now()
            })
            log.insert(ignore_permissions=True)
            frappe.db.commit()
        except Exception as e:
            frappe.log_error(f'Failed to create provisioning log: {str(e)}')
    
    def _send_welcome_email(self, service_doc):
        """Send welcome email to customer"""
        # Implementation using Email Template DocType
        pass
    
    def _send_suspension_email(self, service_doc):
        """Send suspension notification email"""
        # Implementation using Email Template DocType
        pass


# Frappe whitelisted methods for API access
@frappe.whitelist()
def provision_service(service_name):
    """
    Provision a service (called from Service DocType)
    
    Args:
        service_name: Name of Service document
    """
    service = frappe.get_doc('Service', service_name)
    server = frappe.get_doc('Server', service.server)
    
    if server.server_manager == 'cPanel WHM':
        manager = WHMManager(server)
        result = manager.create_account(service)
        return result
    else:
        frappe.throw(_('Unsupported server manager'))


@frappe.whitelist()
def test_server_connection(server_name):
    """
    Test server API connectivity
    
    Args:
        server_name: Name of Server document
    """
    server = frappe.get_doc('Server', server_name)
    
    if server.server_manager == 'cPanel WHM':
        manager = WHMManager(server)
        try:
            packages = manager.list_packages()
            return {
                'success': True,
                'message': f'Connection successful! Found {len(packages)} packages.',
                'packages': packages
            }
        except Exception as e:
            return {
                'success': False,
                'message': str(e)
            }
