# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import frappe.utils
from frappe.utils import cstr, flt, getdate, comma_and, cint,nowdate

class QuotationToOrder(Document):
	def get_quotations(self):
		where = """ docstatus=1 and status = "Open" and customer = "{}" """.format(self.customer)
		if self.from_date :
			where = """{} and transaction_date > "{}" """.format(where,self.from_date)
		if self.to_date :
			where = """{} and transaction_date < "{}" """.format(where,self.to_date)
		quotations=frappe.db.sql("select name, transaction_date,grand_total from tabQuotation where {}".format(where),as_list=1)
		self.set("quotation_list", [])
		for r in quotations:
			pp_so = self.append('quotation_list', {})
			pp_so.quotation = r[0]
			pp_so.date = r[1]
			pp_so.total = r[2]

	def get_items(self):
		so_list = [d.quotation for d in self.get('quotation_list') if d.quotation]
		if not qo_list:
			msgprint(_("Please enter Quotation in the above table"))
		where =""
		
		if self.select_item:
			where = """ and item_code ="{}" """.format(self.select_item)
		items = frappe.db.sql("select item_code , parent, qty,rate,amount,name from `tabQuotation Item` where parent IN ({}) {}".format(tuple(qo_list,where)),as_list=1)
		self.set("items", [])
		for r in quotations:
			pp_so = self.append('items', {})
			pp_so.item = r[0]
			pp_so.quotation = r[1]
			pp_so.qty = r[2]
			pp_so.rate = r[3]
			pp_so.total = r[4]
			pp_so.quotation_item = r[5]
	def create_order(self):
		so = frappe.new_doc("Sales Order")
		so.update({
			"Customer":self.customer,
			"transaction_date":nowdate(),
			"delivery_date":nowdate()
			})
		for data in self.items:
			so.append("items",{
				"item_code": data.item,
				"qty": data.qty,
				"rate": data.rate,
				"amount": data.total,
				"prevdoc_docname": data.quotation,
			})
		return so