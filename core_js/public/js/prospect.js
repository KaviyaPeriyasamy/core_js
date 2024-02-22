// frappe.ui.form.on('Prospect', {
// refresh(frm) {
//         if(cur_frm.doc.__islocal==1 && cur_frm.doc.custom_make_read_only==1){
//                 cur_frm.set_value("custom_make_read_only",0)
//             }
//         if(frm.doc.custom_make_read_only){
//                 setTimeout(()=>{
//                 frm.remove_custom_button("Customer","Create");
//                 frm.remove_custom_button("Opportunity","Create");
//                 frm.remove_custom_button("Call");
//                 frm.remove_custom_button("Next Follow-up");
//                 frm.disable_form();
//         },100)
//         }},
//     set_status_: function(frm){
    
//         if(cur_frm.doc.custom_status=="Converted")
//         {
//                 frm.remove_custom_button("Customer","Create");
//                 frm.remove_custom_button("Opportunity","Create");
//                 frm.remove_custom_button("Call");
//                 frm.remove_custom_button("Next Follow-up");
//         }
	
// },


// })