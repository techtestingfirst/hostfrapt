// Copyright (c) 2026, Praveen Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Hostfrapt Customer", {
	setup: function (frm) {
		frm.set_query("customer_primary_contact", function (doc) {
			return {
				query: "hostfrapt.hostfrapt.doctype.hostfrapt_customer.get_customer_primary",
				filters: {
					customer: doc.name,
					type: "Contact",
				},
			};
		});

		frm.set_query("customer_primary_address", function (doc) {
			return {
				query: "hostfrapt.hostfrapt.doctype.hostfrapt_customer.get_customer_primary",
				filters: {
					customer: doc.name,
					type: "Address",
				},
			};
		});
	},
	customer_primary_address: function (frm) {
		if (frm.doc.customer_primary_address) {
			frappe.call({
				method: "frappe.contacts.doctype.address.address.get_address_display",
				args: {
					address_dict: frm.doc.customer_primary_address,
				},
				callback: function (r) {
					frm.set_value("primary_address", frappe.utils.html2text(r.message));
				},
			});
		}
	},

	customer_primary_contact: function (frm) {
		if (!frm.doc.customer_primary_contact) {
			frm.set_value("mobile_no", "");
			frm.set_value("email_id", "");
		}
	},

	refresh: function (frm) {
		if (!frm.doc.__islocal) {
			frappe.contacts.render_address_and_contact(frm);
			for (const doctype in frm.make_methods) {
				frm.add_custom_button(__(doctype), frm.make_methods[doctype], __("Create"));
			}
		} else {
			frappe.contacts.clear_address_and_contact(frm);
		}
	},
});
