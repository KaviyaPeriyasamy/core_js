// Copyright (c) 2023, Justsigns and contributors
// For license information, please see license.txt

frappe.ui.form.on("Suspect", {
	refresh(frm) {
        if(cur_frm.doc.status=="Prospect" || cur_frm.doc.status== "Junk")
        {
            
        frm.remove_custom_button("Prospect","Create");
        frm.remove_custom_button("Call");
        frm.remove_custom_button("Next Follow-up");
        }
        if(frm.doc.make_read_only){
            setTimeout(()=>{
        frm.remove_custom_button("Prospect","Create");
        frm.remove_custom_button("Call");
        frm.remove_custom_button("Next Follow-up");
    },100)
            frm.disable_form();
        }

        if (!frm.doc.__islocal && frm.doc.docstatus == 0){
            frm.add_custom_button(
                __("Prospect"),
                function () {
                    frappe.call({
                        method: "core_js.core_js.doctype.suspect.suspect.create_prospect",
                        args: {
                            "doc": frm.doc.name
                        },
                        callback: function(r){
                            if (r.message){
                               frappe.set_route('Form', 'Prospect', r.message);
                            }
                        }
                    })
                },
                __("Create")
            );
            }
	},

    status(frm){
       
        if(cur_frm.doc.status=="Prospect" || cur_frm.doc.status== "Junk")
        {
            
        frm.remove_custom_button("Prospect","Create");
        frm.remove_custom_button("Call");
        frm.remove_custom_button("Next Follow-up");
        }
        
    
        if (frm.doc.status == "Prospect"){
            frappe.show_alert({message: "Prospect Status Cannot Set Mannualy.", indicator: 'orange'});
            frm.set_value("status", "Open")
        }
    }
});
