// Copyright (c) 2023, Fadil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rental Booking', {
	refresh: function(frm) {
		let customer = ''
		frappe.db.get_value('Customer',{'mobile_number':frm.doc.phone_number},['name']).then((res)=>{
			console.log(res.message.name)
			customer =res.message.name
		})
		

		frm.add_custom_button(__('Create Rental Order'), function() {
			console.log(typeof frm.doc.pickup_date)
			frappe.route_options={'rental_booking_id':frm.doc.name,'status':'Open','customer':customer ,'pickup_date':frappe.format(frm.doc.pickup_date,{fieldtype:'Date'}),'return_date':frappe.format(frm.doc.return_date,{fieldtype:'Date'})},
			frappe.set_route('Form','Rental Order', 'new-rental-order-1')
		
		});

	}
});
