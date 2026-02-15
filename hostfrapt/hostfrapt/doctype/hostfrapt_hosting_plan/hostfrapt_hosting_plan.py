# Copyright (c) 2025, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptHostingPlan(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		bandwidth_quota: DF.Float
		disk_quota: DF.Float
		ftp_accounts: DF.Int
		max_addon_domains: DF.Int
		max_databases: DF.Int
		max_email_accounts: DF.Int
		max_parked_domains: DF.Int
		max_subdomains: DF.Int
		plan_name: DF.Data
		server_manager: DF.Literal["", "cPanel", "DirectAdmin", "Proxmox", "Custom"]
		ssh_access: DF.Check
	# end: auto-generated types

	pass
