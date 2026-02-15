# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HostfraptPricingTable(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		billing_cycle: DF.Data | None
		billing_plan: DF.Link
		currency: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		price: DF.Currency
		setup_fee: DF.Currency
		total: DF.ReadOnly | None
	# end: auto-generated types

	pass