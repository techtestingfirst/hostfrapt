# Copyright (c) 2025, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptProduct(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		activation: DF.Literal["After order is placed", "After payment is received", "Manual activation"]
		enable_stock: DF.Check
		enabled: DF.Check
		hidden: DF.Check
		hosting_plan: DF.Link
		name: DF.Int | None
		product_type: DF.Literal["Hosting", "Domain", "License", "Downloadable"]
		quantity_in_stock: DF.Int
		route: DF.Data | None
		server_allocation: DF.Link | None
		title: DF.Data
	# end: auto-generated types

	pass
