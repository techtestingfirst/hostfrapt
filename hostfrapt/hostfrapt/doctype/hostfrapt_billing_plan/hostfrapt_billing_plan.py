# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptBillingPlan(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		billing_type: DF.Literal["", "Free", "Trial", "One Time", "Recurring"]
		currency: DF.Link | None
		enabled: DF.Check
		name: DF.Int | None
		price: DF.Currency
		term_period: DF.Link | None
		title: DF.Data
		trial_period: DF.Int
	# end: auto-generated types

	pass
