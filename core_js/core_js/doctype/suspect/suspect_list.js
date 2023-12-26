frappe.listview_settings['Suspect'] = {
	add_fields: ["status"],
	get_indicator: function (doc) {
		if (doc.status === "Junck") {
			return [__("Junck"), "orange", "status,=,Junck"];
		} 
        
        else if (doc.status === "Lead") {
			return [__("Lead"), "green", "status,=,Lead"];
		}

        else if (doc.status === "Open") {
			return [__("Open"), "blue", "status,=,Open"];
		}

	}
};
