import frappe
import requests
from frappe import _
import json

class DirectAdminManager:
    """DirectAdmin API Manager for account provisioning"""
    
    def __init__(self, server_doc):
        """
        Initialize DirectAdmin Manager
        
        Args:
            server_doc: Server DocType document
        """
        self.server = server_doc
        self.hostname = server_doc.hostname
        self.api_user = server_doc.api_username or 'admin'
        self.api_password = server_doc.get_password('api_password')
        self.base_url = f"https://{self.hostname}:2222"
        
    def _make_request(self, endpoint, method='POST', data=None):
        """
        Make authenticated API request to DirectAdmin
        
        Args:
            endpoint: API endpoint
            method: HTTP method (GET/POST)
            data: Request data
            
        Returns:
            dict: API response
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.request(
                method,
                url,
                auth=(self.api_user, self.api_password),
                data=data,
                verify=True,
                timeout=30
            )
            response.raise_for_status()
            
            # DirectAdmin returns URL-encoded or plain text responses
            result = dict(item.split('=') for item in response.text.split('&') if '=' in item)
            
            # Log the API call
            self._log_provisioning(endpoint, data, result, 'Success')
            
            return result
            
        except Exception as e:
            error_msg = str(e)
            self._log_provisioning(endpoint, data, {'error': error_msg}, 'Failed')
            frappe.throw(_('DirectAdmin API Error: {0}').format(error_msg))
    
    def create_account(self, service_doc):
        """
        Create DirectAdmin account
        
        Args:
            service_doc: Service DocType document
            
        Returns:
            dict: Creation result
        """
        product = frappe.get_doc('Hosting Product', service_doc.product)
        plan = frappe.get_doc('Hosting Plan', product.hosting_plan)
        
        # Generate username (max 10 chars for DirectAdmin)
        domain = service_doc.domain_name
        username = domain.replace('.', '')[:10]
        
        # Generate password
        password = frappe.generate_hash(length=16)
        email = service_doc.customer_email
        
        data = {
            'action': 'create',
            'add': 'Submit',
            'username': username,
            'email': email,
            'passwd': password,
            'passwd2': password,
            'domain': domain,
            'package': plan.plan_name,  # Must match DirectAdmin package
            'ip': service_doc.dedicated_ip or 'shared',
            'notify': 'yes'  # Send welcome email
        }
        
        result = self._make_request('/CMD_API_ACCOUNT_USER', method='POST', data=data)
        
        if result.get('error') == '0':
            # Update service
            service_doc.username = username
            service_doc.set_password('password', password)
            service_doc.control_panel_url = f"https://{domain}:2222"
            service_doc.service_status = 'Active'
            service_doc.save(ignore_permissions=True)
            
            return {
                'success': True,
                'username': username,
                'password': password,
                'message': 'Account created successfully'
            }
        else:
            frappe.throw(_('Account creation failed: {0}').format(
                result.get('text', 'Unknown error')
            ))
    
    def suspend_account(self, service_doc):
        """Suspend DirectAdmin account"""
        data = {
            'action': 'suspend',
            'select0': service_doc.username
        }
        
        result = self._make_request('/CMD_API_SELECT_USERS', method='POST', data=data)
        
        if result.get('error') == '0':
            service_doc.service_status = 'Suspended'
            service_doc.save(ignore_permissions=True)
            return {'success': True, 'message': 'Account suspended'}
        else:
            frappe.throw(_('Suspension failed'))
    
    def unsuspend_account(self, service_doc):
        """Unsuspend DirectAdmin account"""
        data = {
            'action': 'unsuspend',
            'select0': service_doc.username
        }
        
        result = self._make_request('/CMD_API_SELECT_USERS', method='POST', data=data)
        
        if result.get('error') == '0':
            service_doc.service_status = 'Active'
            service_doc.save(ignore_permissions=True)
            return {'success': True, 'message': 'Account unsuspended'}
        else:
            frappe.throw(_('Unsuspension failed'))
    
    def terminate_account(self, service_doc):
        """Terminate DirectAdmin account"""
        data = {
            'confirmed': 'Confirm',
            'delete': 'yes',
            'select0': service_doc.username
        }
        
        result = self._make_request('/CMD_API_SELECT_USERS', method='POST', data=data)
        
        if result.get('error') == '0':
            service_doc.service_status = 'Terminated'
            service_doc.termination_date = frappe.utils.now()
            service_doc.save(ignore_permissions=True)
            return {'success': True, 'message': 'Account terminated'}
        else:
            frappe.throw(_('Termination failed'))
    
    def change_package(self, service_doc, new_package):
        """Change DirectAdmin package"""
        data = {
            'action': 'package',
            'package': new_package,
            'select0': service_doc.username
        }
        
        result = self._make_request('/CMD_API_SELECT_USERS', method='POST', data=data)
        
        if result.get('error') == '0':
            return {'success': True, 'message': 'Package changed'}
        else:
            frappe.throw(_('Package change failed'))
    
    def _log_provisioning(self, action, request_data, response_data, status):
        """Log provisioning action"""
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
