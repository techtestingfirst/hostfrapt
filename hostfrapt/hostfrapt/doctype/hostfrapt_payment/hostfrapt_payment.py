# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptPayment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from hostfrapt.hostfrapt.doctype.hostfrapt_applied_to_invoice.hostfrapt_applied_to_invoice import HostfraptAppliedToInvoice

		amount_paid: DF.Currency
		applied_to_invoices: DF.Table[HostfraptAppliedToInvoice]
		currency: DF.Link | None
		customer: DF.Link | None
		gateway: DF.Literal["", "Stripe", "Razorpay", "PayPal"]
		notes: DF.SmallText | None
		payment_balance: DF.Currency
		payment_date: DF.Date | None
		payment_method: DF.Literal["", "Cash", "UPI", "Credit Card", "Bank Transfer", "Credits"]
		payment_number: DF.Data | None
		receipt: DF.Data | None
		transaction_id: DF.Data | None
		transaction_status: DF.Literal["Success", "Pending", "Failed"]
	# end: auto-generated types

	pass
