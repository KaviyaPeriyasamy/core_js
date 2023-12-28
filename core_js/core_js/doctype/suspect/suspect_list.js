frappe.listview_settings['Suspect'] = {
	add_fields: ["status"],
	get_indicator: function (doc) {
		if (doc.status === "Junk") {
			return [__("Junk"), "orange", "status,=,Junk"];
		} 
        
        else if (doc.status === "Prospect") {
			return [__("Prospect"), "green", "status,=,Prospect"];
		}

        else if (doc.status === "Open") {
			return [__("Open"), "blue", "status,=,Open"];
		}

	}
};
