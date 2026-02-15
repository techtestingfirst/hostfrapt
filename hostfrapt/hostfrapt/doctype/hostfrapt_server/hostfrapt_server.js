// Copyright (c) 2025, Praveen Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Hostfrapt Server", {
	refresh(frm) {
        frm.add_custom_button('Test Connection', () => console.log('Connection Tested'));
},
});
