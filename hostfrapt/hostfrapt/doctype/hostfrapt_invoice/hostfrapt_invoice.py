# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptInvoice(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from hostfrapt.hostfrapt.doctype.hostfrapt_invoice_item.hostfrapt_invoice_item import HostfraptInvoiceItem

		amount_paid: DF.Currency
		balance_due: DF.Currency
		customer: DF.Link | None
		due_date: DF.Date | None
		invoice_date: DF.Date | None
		invoice_items: DF.Table[HostfraptInvoiceItem]
		invoice_number: DF.Data | None
		invoice_status: DF.Literal["Draft", "Unpaid", "Paid", "Cancelled", "Refunded", "Partially Paid"]
		late_fee_applied: DF.Currency
		notes: DF.SmallText | None
		payment_date: DF.Date | None
		payment_link: DF.Data | None
		payment_method: DF.Data | None
		subtotal: DF.Currency
		tax_amount: DF.Currency
	# end: auto-generated types

	pass
