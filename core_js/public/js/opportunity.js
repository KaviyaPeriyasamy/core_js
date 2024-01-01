
frappe.ui.form.on('Opportunity', {
    refresh(frm) {
        if(frm.doc.custom_make_read_only){
            frm.disable_form();
            setTimeout(()=>{
                frm.remove_custom_button("Supplier Quotation","Create");
                frm.remove_custom_button("Request For Quotation","Create");
                frm.remove_custom_button("Quotation","Create");
                frm.remove_custom_button("Customer","Create");
                frm.remove_custom_button("Call");
                frm.remove_custom_button("Close");
                frm.remove_custom_button("Next Follow-up");
            },100)
        }},
    status: function(frm){
    
        if(cur_frm.doc.status=="Converted")
        {
            
                frm.remove_custom_button("Supplier Quotation","Create");
                frm.remove_custom_button("Request For Quotation","Create");
                frm.remove_custom_button("Quotation","Create");
                frm.remove_custom_button("Call");
                frm.remove_custom_button("Close");
                frm.remove_custom_button("Next Follow-up");
        }
	
    },})
frappe.ui.form.on('Opportunity Item', {

   item_code:function(frm,cdt,cdn){
    let row= locals[cdt][cdn];
    frappe.db.get_list('Item Price',{filters: {item_code: row.item_code,price_list:frm.doc.price_list}, fields: ['price_list_rate'], pluck: "price_list_rate"}).then((res) => {
    if(res){
        frappe.model.set_value(cdt, cdn, "rate", res[0]);
    }
    else{
     frappe.model.set_value(cdt, cdn, "rate", "");
    }
    })
}
})
