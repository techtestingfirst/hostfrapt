# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptOrder(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from hostfrapt.hostfrapt.doctype.hostfrapt_order_items.hostfrapt_order_items import HostfraptOrderItems

		address: DF.Link | None
		amended_from: DF.Link | None
		currency: DF.Link | None
		fraud_score: DF.Percent
		invoice: DF.Data | None
		next_due_date: DF.Date | None
		notes: DF.SmallText | None
		order_date: DF.Date | None
		order_items: DF.Table[HostfraptOrderItems]
		order_number: DF.Data | None
		order_status: DF.Literal["Pending", "Accepted", "Provisioning", "Active", "Cancelled", "Fraude"]
		order_total: DF.Currency
		payment_method: DF.Data | None
		payment_status: DF.Literal["Unpaid", "Paid", "Refunded"]
		referred_by: DF.Data | None
		user: DF.Link | None
	# end: auto-generated types

	pass
