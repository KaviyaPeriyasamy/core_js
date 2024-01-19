frappe.ui.form.on('Lead', {
    
    refresh(frm) {
        if(cur_frm.doc.__islocal==1&&cur_frm.doc.custom_make_read_only==1){
            cur_frm.set_value("custom_make_read_only",0)
        }
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
        }
        else{
            frm.add_custom_button(
                __("Prospect"),
                function () {
                    frappe.call({
                        method: "core_js.core_js.utils.leads.create_prospect",
                        args: {
                            "doc": frm.doc.name
                        },
                        callback: async function(r){
                            if (r.message){
                                // await frm.refresh();
                                await cur_frm.reload_doc();
                               frappe.set_route('Form', 'Prospect', r.message);
                               
                            }
                        }
                    })
                },
                __("Create")
            );
            
        }},
        
    status: function(frm){
    
        if(cur_frm.doc.status=="Converted"|| cur_frm.doc.status=="Prospect")
        {
                frm.remove_custom_button("Customer","Create");
                frm.remove_custom_button("Opportunity","Create");
                frm.remove_custom_button("Quotation","Create");
                frm.remove_custom_button("Prospcet","Create");
                frm.remove_custom_button("Call");
                frm.remove_custom_button("Next Follow-up");
        }
	
    },})