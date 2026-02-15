# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptService(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		auto_suspend: DF.Check
		billing_cycle: DF.Link | None
		control_panel_login_url: DF.Data | None
		customer: DF.Link | None
		dedicated_ip: DF.Data | None
		domain_name: DF.Data | None
		next_due_date: DF.Date | None
		order: DF.Link | None
		password: DF.Password | None
		product: DF.Link | None
		recurring_amount: DF.Currency
		registration_date: DF.Link | None
		server: DF.Link | None
		service_id: DF.Data | None
		service_metadata: DF.JSON | None
		service_status: DF.Literal["Pending", "Active", "Suspended", "Terminated", "Cancelled"]
		suspension_reason: DF.SmallText | None
		termination_date: DF.Date | None
		username: DF.Data | None
	# end: auto-generated types

	pass
