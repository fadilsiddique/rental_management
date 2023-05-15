# Copyright (c) 2023, Fadil and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class RentalBooking(Document):
	
	def after_insert(self):
		existing_customer=frappe.db.exists({"doctype":"Customer","mobile_number":self.phone_number})
		if not existing_customer:

			customer = frappe.get_doc({
				'doctype':'Customer',
				'customer_name':self.name1,
				'mobile_number':self.phone_number,
				'customer_group':'Individual',
				'territory':'India'
			})

			customer.insert(ignore_permissions=True)
			customer.save(ignore_permissions=True)

	





