// Copyright (c) 2023, Justsigns and contributors
// For license information, please see license.txt

frappe.ui.form.on("Suspect", {
	refresh(frm) {
        frm.add_custom_button(
            __("Lead"),
            function () {
                // erpnext.utils.map_current_doc({
				// 	method: "core_js.core_js.doctype.suspect.suspect.create_lead",
				// 	source_doctype: "Suspect",
				// 	target: frm,
				// })
                // frappe.call({
                //     method: "core_js.core_js.doctype.suspect.suspect.create_lead",
                //     args: {
                //         "doc_name": frm.doc.name
                //     }
                // })
            },
            __("Create")
        );
	},
});