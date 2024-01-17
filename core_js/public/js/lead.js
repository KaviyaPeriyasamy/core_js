frappe.ui.form.on('Lead', {
    refresh(frm) {
        frm.add_custom_button(
            __("Prospect"),
            function () {
                frappe.call({
                    method: "core_js.core_js.utils.leads.create_prospect",
                    args: {
                        "doc": frm.doc.name
                    },
                    callback: function(r){
                        if (r.message){cur_frm.set_value("status","Prospect")
                           frappe.set_route('Form', 'Prospect', r.message);
                        }
                    }
                })
            },
            __("Create")
        );
        if(cur_frm.doc.custom_make_read_only){
            setTimeout(()=>{
            frm.remove_custom_button("Customer","Create");
            frm.remove_custom_button("Opportunity","Create");
            frm.remove_custom_button("Quotation","Create");
            frm.remove_custom_button("Prospcet","Create");
            frm.remove_custom_button("Call");
            frm.remove_custom_button("Next Follow-up");
        },100)
            frm.disable_form();

            
        }},
    status: function(frm){
    
        if(cur_frm.doc.status=="Converted")
        {
                frm.remove_custom_button("Customer","Create");
                frm.remove_custom_button("Opportunity","Create");
                frm.remove_custom_button("Quotation","Create");
                frm.remove_custom_button("Prospcet","Create");
                frm.remove_custom_button("Call");
                frm.remove_custom_button("Next Follow-up");
        }
	
    },})