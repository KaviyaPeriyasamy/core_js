// Copyright (c) 2023, Justsigns and contributors
// For license information, please see license.txt

frappe.ui.form.on("Suspect", {
	refresh(frm) {

        if (!frm.doc.__islocal && frm.doc.docstatus == 0){
            frm.add_custom_button(
                __("Lead"),
                function () {
                    frappe.call({
                        method: "core_js.core_js.doctype.suspect.suspect.create_lead",
                        args: {
                            "doc": frm.doc.name
                        },
                        callback: function(r){
                            if (r.message){
                               frappe.set_route('Form', 'Lead', r.message);
                            }
                        }
                    })
                },
                __("Create")
            );
            }
	},

    status(frm){
        if (frm.doc.status == "Lead"){
            frappe.show_alert({message: "Lead Status Cannot Set Mannualy.", indicator:'orange'});
            frm.set_value("status", "Open")
        }
    }
});
