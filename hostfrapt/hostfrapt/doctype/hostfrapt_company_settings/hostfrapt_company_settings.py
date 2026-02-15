# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptCompanySettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address_details: DF.Link | None
		auto_suspension: DF.Check
		auto_termination: DF.Check
		company_logo: DF.AttachImage | None
		company_name: DF.Data | None
		default_currency: DF.Link | None
		default_tax_template: DF.Data | None
		email: DF.Data | None
		invoice_number_series: DF.Int
		invoice_prefix: DF.Data | None
		late_fee_after_days: DF.Int
		late_fee_amount: DF.Currency
		late_fee_settings: DF.Check
		late_fee_type: DF.Literal["", "Percentage", "Fix Amount"]
		phone: DF.Phone | None
		suspension_after_days: DF.Int
		tax_id: DF.Data | None
		termination_after_days: DF.Int
	# end: auto-generated types

	pass
