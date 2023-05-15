// Copyright (c) 2023, Fadil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rental Order', {
    refresh: function(frm) {

		let items = []

		frm.doc.rental_items.map((event)=>{
			let item = {
				'item_code':event.item,
				'qty':event.quantity
			}
			items.push(item)
		})
		let data = {
			'customer':frm.doc.customer,
			'rental_order_id':frm.doc.name,
			'items':items
		}
        frm.add_custom_button(__('Create Sales Invoice'), function() {
			let salesInvoiceId = ''

			frappe.call({
				method:'rental_management.rental_management.doctype.rental_order.rental_order.make_sales_invoice',
				args:{
					data:data
				},
				callback:(res)=>{
					salesInvoiceId = res.message.name
					frappe.set_route('Form','Sales Invoice',salesInvoiceId)
				}
			})
				

    });

   // Add more buttons here

    }
});
