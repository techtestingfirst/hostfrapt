# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptServiceAddonInstance(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		activation_date: DF.Date | None
		addon: DF.Link | None
		billing_cycle: DF.Data | None
		billing_plan: DF.Link | None
		next_due_date: DF.Date | None
		price: DF.Currency
		quantity: DF.Int
		service: DF.Link | None
		setup_fee: DF.Currency
		status: DF.Literal["Active", "Cancelled"]
		total: DF.Currency
	# end: auto-generated types

	pass
