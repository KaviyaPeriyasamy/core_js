frappe.ui.form.on('Prospect', {
refresh(frm) {
        if(frm.doc.custom_make_read_only){
                frm.disable_form();
        }},
    set_status_: function(frm){
    
        if(cur_frm.doc.stek_status_=="Converted")
        {
                frm.remove_custom_button("Customer","Create");
                frm.remove_custom_button("Opportunity","Create");
                frm.remove_custom_button("Call");
                frm.remove_custom_button("Next Follow-up");
        }
	
},})