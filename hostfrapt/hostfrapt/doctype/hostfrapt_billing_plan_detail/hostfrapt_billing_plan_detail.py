# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptBillingPlanDetail(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		billing_type: DF.ReadOnly | None
		currency: DF.ReadOnly | None
		name: DF.Int | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		price: DF.ReadOnly | None
		term_period: DF.ReadOnly | None
		title: DF.Link
	# end: auto-generated types

	pass
