# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptServiceAddon(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from hostfrapt.hostfrapt.doctype.hostfrapt_pricing_table.hostfrapt_pricing_table import HostfraptPricingTable

		addon_name: DF.Data | None
		addon_type: DF.Literal["Disk Space", "Bandwidth", "IP Address", "SSL", "Backup"]
		applicable_to_products: DF.Link | None
		pricing: DF.Table[HostfraptPricingTable]
		provisioning_module: DF.Data | None
		provisioning_required: DF.Check
	# end: auto-generated types

	pass
