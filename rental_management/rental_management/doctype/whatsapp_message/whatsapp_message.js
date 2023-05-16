// Copyright (c) 2023, Fadil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Whatsapp Message', {
	refresh: function(frm) {
		if(!frm.doc.message_id){
			const btn = frm.add_custom_button("Send Message",()=>{
				frm
				   .call({
					doc:frm.doc,
					method:"send",
					btn
				   })
				   .then((m)=>frm.refresh())
			})
			
		}

	}
});
