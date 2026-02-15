# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptCustomerCredit(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from hostfrapt.hostfrapt.doctype.hostfrapt_credit_transaction.hostfrapt_credit_transaction import HostfraptCreditTransaction

		available_credit: DF.Currency
		credit_transactions: DF.Table[HostfraptCreditTransaction]
		currency: DF.Link | None
		customer: DF.Link | None
	# end: auto-generated types

	pass
