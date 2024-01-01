frappe.listview_settings['Prospect'] = {
	add_fields: ["custom_status"],
	
	get_indicator: function(doc) {
		if (doc.custom_status=="New") {
			return [__("New"), "orange", "custom_status,=,New"];
        }
		else if (doc.custom_status=="Converted") {
			return [__("Converted"), "green", "custom_status,=,Converted"];
        }
		else if (doc.custom_status=="Interested") {
			return [__("Interested"), "blue", "custom_status,=,Interested"];
        }
		else if (doc.custom_status=="Following Up") {
			return [__("Following Up"), "purple", "custom_status,=,Following Up"];
        }
		else if (doc.custom_status=="Unqualified") {
			return [__("Unqualified"), "red", "custom_status,=,Unqualified"];
        }
		else if (doc.custom_status=="Sample Sent") {
			return [__("Sample Sent"), "gray", "custom_status,=,Sample Sent"];
        }
		else if (doc.custom_status=="Sample to be sent") {
			return [__("Sample to be sent"), "yellow", "custom_status,=,Sample to be sent"];
        }
		else if (doc.custom_status=="Opportunity") {
			return [__("Opportunity"), "pink", "custom_status,=,Opportunity"];
        }
		
	},
	
};
