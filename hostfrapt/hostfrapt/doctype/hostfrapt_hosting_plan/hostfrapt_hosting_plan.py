# Copyright (c) 2025, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HostfraptHostingPlan(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from hostfrapt.hostfrapt.doctype.hostfrapt_billing_plan_detail.hostfrapt_billing_plan_detail import HostfraptBillingPlanDetail

		billing_plan: DF.Table[HostfraptBillingPlanDetail]
		name: DF.Int | None
		plan_discription: DF.TextEditor | None
		plan_name: DF.Data
	# end: auto-generated types

	pass
