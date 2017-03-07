// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quotation To Order', {
	refresh: function(frm) {

	},
	get_quotation: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "get_quotation",
			callback: function(r) {
				refresh_field("quotation_list");
			}
		});
	},
	get_item: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "get_item",
			callback: function(r) {
				refresh_field("items");
			}
		});
	},
});
