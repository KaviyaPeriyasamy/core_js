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
