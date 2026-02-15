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
		from hostfrapt.hostfrapt.doctype.hostfrapt_pricing_table.hostfrapt_pricing_table import HostfraptPricingTable

		allocation_server: DF.Link | None
		auto_setup: DF.Check
		description: DF.Text | None
		pricing_table: DF.Table[HostfraptPricingTable]
		product_name: DF.Data
		product_type: DF.Literal["", "Shared Hosting", "VPS", "Dedicated", "Cloud", "Domain", "SSL", "Addon"]
		quantity_in_stock: DF.Int
		resource_limits: DF.Link | None
		server_manager_type: DF.ReadOnly | None
		stock_control: DF.Check
	# end: auto-generated types

	def validate(self):
		self.set_total()

	# set the total price for each row in the pricing table
	def set_total(self):
		for row in self.pricing_table:
			if not row.setup_fee:
				row.total = row.price
			else:
				row.total = row.price + row.setup_fee
	
	
	