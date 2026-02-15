# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptDomain(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from hostfrapt.hostfrapt.doctype.hostfrapt_nameserver.hostfrapt_nameserver import HostfraptNameserver

		auto_renew: DF.Check
		customer: DF.Link | None
		domain_name: DF.Data | None
		domain_status: DF.Literal["Active", "Pending", "Transfer", "Expired", "Locked"]
		epp_code: DF.Data | None
		expiry_date: DF.Date | None
		nameservers: DF.Table[HostfraptNameserver]
		registrar: DF.Data | None
		registration_date: DF.Date | None
		whois_privacy_enabled: DF.Check
		years_registered: DF.Int
	# end: auto-generated types

	pass
