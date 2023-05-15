// Copyright (c) 2023, Fadil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rental Order', {
    refresh: function(frm) {
        frm.add_custom_button(__('Create Sales Invoice'), function() {

        console.log('hello')});	


        // Add more buttons here

    }
});
