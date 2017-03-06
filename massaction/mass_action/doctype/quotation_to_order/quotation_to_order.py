# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QuotationToOrder(Document):
	def get_quotation(self):
		where = """ docstatus=1 and status = "Open" and customer = "{}" """.format(self.customer)
		if self.from_date :
			where = """{} and transaction_date > "{}" """.format(self.from_date)
		if self.to_date :
			where = """{} and transaction_date < "{}" """.format(self.to_date)
		quotations=frappe.db.sql("select name, transaction_date,grand_total from tabQuotation where {}".format(where),as_list=1)
		self.set("quotation_list", [])
		for r in quotations:
			pp_so = self.append('quotation_list', {})
			pp_so.quotation = r['name']
			pp_so.date = r['transaction_date']
			pp_so.grand_total = r['grand_total']

	def get_item(self):
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
			pp_so.item = r['item_code']
			pp_so.quotation = r['parent']
			pp_so.qty = r['qty']
			pp_so.rate = r['rate']
			pp_so.total = r['amount']
			pp_so.quotation_item = r['name']