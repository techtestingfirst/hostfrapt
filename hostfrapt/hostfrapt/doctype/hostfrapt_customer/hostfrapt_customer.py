# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.contacts.address_and_contact import (
	delete_contact_and_address,
	load_address_and_contact,
)

class HostfraptCustomer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		account_status: DF.Literal["Active", "Suspended", "Terminated"]
		address_line_1: DF.Data | None
		address_line_2: DF.Data | None
		city: DF.Data | None
		company_name: DF.Data | None
		country: DF.Link | None
		customer_type: DF.Literal["Individual", "Business"]
		first_name: DF.Data | None
		full_name: DF.Data | None
		last_name: DF.Data | None
		middle_name: DF.Data | None
		mobile_no: DF.Phone | None
		naming_series: DF.Literal["CUST-.YYYY.-"]
		postal_code: DF.Data | None
		salutation: DF.Link | None
		state: DF.Data | None
		tax_id: DF.Data | None
		time_zone: DF.Data | None
		user: DF.Link | None
	# end: auto-generated types

def on_update(self):
	self.create_primary_contact()
	self.create_primary_address()

	if self.flags.is_new_doc:
		self.link_address_and_contact()
		self.copy_communication()

def create_primary_contact(self):
		if not self.customer_primary_contact and not self.lead_name:
			if self.mobile_no or self.email_id or self.first_name or self.last_name:
				contact = make_contact(self)
				self.db_set("customer_primary_contact", contact.name)
				self.db_set("mobile_no", self.mobile_no)
				self.db_set("email_id", self.email_id)
		elif self.customer_primary_contact:
			frappe.set_value("Contact", self.customer_primary_contact, "is_primary_contact", 1)  # ensure


def create_primary_address(self):
	from frappe.contacts.doctype.address.address import get_address_display

	if self.flags.is_new_doc and self.get("address_line1"):
		address = make_address(self)
		address_display = get_address_display(address.name)

		self.db_set("customer_primary_address", address.name)
		self.db_set("primary_address", address_display)
	elif self.customer_primary_address:
		frappe.set_value("Address", self.customer_primary_address, "is_primary_address", 1)  # ensure

def make_contact(args, is_primary_contact=1):
	values = {
		"doctype": "Contact",
		"is_primary_contact": is_primary_contact,
		"links": [{"link_doctype": args.get("doctype"), "link_name": args.get("name")}],
	}

	party_type = args.customer_type if args.doctype == "Customer" else args.supplier_type
	party_name_key = "customer_name" if args.doctype == "Customer" else "supplier_name"

	if party_type == "Individual":
		first, middle, last = parse_full_name(args.get(party_name_key))
		values.update(
			{
				"first_name": first,
				"middle_name": middle,
				"last_name": last,
			}
		)
	else:
		values.update(
			{
				"company_name": args.get(party_name_key),
			}
		)

	contact = frappe.get_doc(values)

	if args.get("email_id"):
		contact.add_email(args.get("email_id"), is_primary=True)
	if args.get("mobile_no"):
		contact.add_phone(args.get("mobile_no"), is_primary_mobile_no=True)
	if args.get("first_name"):
		contact.first_name = args.get("first_name")
	if args.get("last_name"):
		contact.last_name = args.get("last_name")

	if flags := args.get("flags"):
		contact.insert(ignore_permissions=flags.get("ignore_permissions"))
	else:
		contact.insert()

	return contact


def make_address(args, is_primary_address=1, is_shipping_address=1):
	reqd_fields = []
	for field in ["city", "country"]:
		if not args.get(field):
			reqd_fields.append("<li>" + field.title() + "</li>")

	if reqd_fields:
		msg = _("Following fields are mandatory to create address:")
		frappe.throw(
			"{} <br><br> <ul>{}</ul>".format(msg, "\n".join(reqd_fields)),
			title=_("Missing Values Required"),
		)

	party_name_key = "customer_name" if args.doctype == "Customer" else "supplier_name"

	address = frappe.get_doc(
		{
			"doctype": "Address",
			"address_title": args.get(party_name_key),
			"address_line1": args.get("address_line1"),
			"address_line2": args.get("address_line2"),
			"city": args.get("city"),
			"state": args.get("state"),
			"pincode": args.get("pincode"),
			"country": args.get("country"),
			"is_primary_address": is_primary_address,
			"is_shipping_address": is_shipping_address,
			"links": [{"link_doctype": args.get("doctype"), "link_name": args.get("name")}],
		}
	)

	if flags := args.get("flags"):
		address.insert(ignore_permissions=flags.get("ignore_permissions"))
	else:
		address.insert()

	return address

def parse_full_name(full_name: str) -> tuple[str, str | None, str | None]:
	"""Parse full name into first name, middle name and last name"""
	names = full_name.split()
	first_name = names[0]
	middle_name = " ".join(names[1:-1]) if len(names) > 2 else None
	last_name = names[-1] if len(names) > 1 else None

	return first_name, middle_name, last_name
