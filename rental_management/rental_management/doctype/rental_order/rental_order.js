// Copyright (c) 2023, Fadil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rental Order', {
	validate: function(frm) {
        if (frm.doc.pickup_date < get_today()) {
            frappe.throw(__("Please select a Pickup Date from the present or future."));
        }
    },
	pickup_date: function(frm) {
        if (!frm.doc.return_date) {
            frm.set_value("return_date", frm.doc.pickup_date);
        }

        frm.fields_dict.return_date.datepicker.update({
            minDate: frm.doc.pickup_date ? new Date(frm.doc.pickup_date) : null
        });
    },
	return_date: function(frm) {
        frm.fields_dict.pickup_date.datepicker.update({
            maxDate: frm.doc.return_date ? new Date(frm.doc.return_date) : null
        });
    },
    refresh: function(frm) {
		frm.fields_dict.pickup_date.datepicker.update({
			minDate: new Date(frappe.datetime.get_today()),
			})
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
