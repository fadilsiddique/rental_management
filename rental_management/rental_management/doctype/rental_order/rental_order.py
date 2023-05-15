# Copyright (c) 2023, Fadil and contributors
# For license information, please see license.txt
import json
import frappe
from frappe.model.document import Document

class RentalOrder(Document):
	pass

@frappe.whitelist()

def make_sales_invoice(data):
	data=json.loads(data)
	print(data['items'])
	new_invoice=frappe.get_doc({
		'doctype':'Sales Invoice',
		'customer':data['customer'],
		'rental_order_id':data['rental_order_id'],
		'items':data['items']
	})

	new_invoice.insert(ignore_permissions=True)
	new_invoice.save(ignore_permissions=True)

	return new_invoice
