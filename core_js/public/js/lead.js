frappe.ui.form.on('Lead', {
    refresh(frm) {
        if(frm.doc.custom_make_read_only){
            frm.disable_form();
        }},
    status: function(frm){
    
        if(cur_frm.doc.status=="Converted")
        {
                frm.remove_custom_button("Customer","Create");
                frm.remove_custom_button("Opportunity","Create");
                frm.remove_custom_button("Quotation","Create");
                frm.remove_custom_button("Call");
                frm.remove_custom_button("Next Follow-up");
        }
	
    },})