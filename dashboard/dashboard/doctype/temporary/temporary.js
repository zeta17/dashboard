// Copyright (c) 2019, hendrik and contributors
// For license information, please see license.txt

frappe.ui.form.on('Temporary', {
	refresh: function(frm) {

	},
	on_submit: function(frm){
		frappe.set_route("List", "Sales Invoice");
	},
});
