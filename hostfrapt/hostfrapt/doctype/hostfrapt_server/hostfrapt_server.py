# Copyright (c) 2025, Praveen Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HostfraptServer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		assigned_ip_addresses: DF.Data | None
		connection_port: DF.Data
		hostname: DF.Data
		ip: DF.Data
		is_enabled: DF.Check
		name: DF.Int | None
		name_server_1: DF.Data
		name_server_2: DF.Data
		name_server_3: DF.Data | None
		name_server_4: DF.Data | None
		password_length: DF.Int
		password_or_login_key: DF.Data
		server_location: DF.Link | None
		server_name: DF.Data
		server_panel: DF.Literal["", "Direct Admin", "C Panel", "Plesk", "CWP"]
		server_provider: DF.Data | None
		use_secure_connection: DF.Check
		username: DF.Data
	# end: auto-generated types

	pass
