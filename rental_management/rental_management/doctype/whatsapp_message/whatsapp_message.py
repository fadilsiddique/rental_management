# Copyright (c) 2023, Fadil and contributors
# For license information, please see license.txt

import frappe
import requests
import mimetypes
from frappe.model.document import Document
from typing import Dict

class WhatsappMessage(Document):
	
	@frappe.whitelist()
	def send(self) -> Dict:

		if not self.to:
			frappe.throw("Recepient (`to`) is required to send message.")

		access_token = frappe.db.get_single_value('Whatsapp settings', "access_token")
		api_base_url = "https://graph.facebook.com/v16.0"
		phone_number_id = frappe.db.get_single_value('Whatsapp settings','phone_number_id')

		endpoint = f"{api_base_url}/{phone_number_id}/messages"
		print(endpoint)
		response_data = {
			"messaging_product": "whatsapp",
			"recipient_type": "individual",
			"to": self.to,
			"type":self.message_type.lower(),
		}

		if self.message_type == 'Text':
			response_data['text']={"preview_url": False, "body": self.message_body}
		try:
			response = requests.post(
				endpoint,
				json=response_data,
				headers={
					"Authorization":"Bearer " + access_token,
					"Content-Type": "application/json",
				}
			)

			print(response,"helllooo")

			if response.ok:
				self.message_id = response.json().get("messages")[0]["id"]
				self.save(ignore_permissions=True)
				return response.json()

			else:
				frappe.throw(response.json().get("error").get("message"))

		except Exception as e:
			print(e)
			frappe.throw(e)



		

