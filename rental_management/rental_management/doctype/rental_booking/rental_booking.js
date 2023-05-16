// Copyright (c) 2023, Fadil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rental Booking', {
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
		let customer = ''
		frappe.db.get_value('Customer',{'mobile_number':frm.doc.phone_number},['name']).then((res)=>{
			console.log(res.message.name)
			customer =res.message.name
		})
		

		frm.add_custom_button(__('Create Rental Order'), function() {
			frappe.route_options={'rental_booking_id':frm.doc.name,'status':'Open','customer':customer ,'pickup_date':frappe.format(frm.doc.pickup_date,{fieldtype:'Date'}),'return_date':frappe.format(frm.doc.return_date,{fieldtype:'Date'})},
			frappe.set_route('Form','Rental Order', 'new-rental-order-1')
		
		});

	}
});
