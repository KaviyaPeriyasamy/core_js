frappe.listview_settings['Prospect'] = {
	add_fields: ["custom_status"],
	
	get_indicator: function(doc) {
		if (doc.stek_status_=="New") {
			return [__("New"), "green", "stek_status_,=,New"];
        }
		
	},
	
};
