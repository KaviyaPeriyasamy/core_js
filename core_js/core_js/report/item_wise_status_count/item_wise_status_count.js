// Copyright (c) 2023, ts@gmail.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Item-Wise Status Count"] = {
	"filters": [

		{
			"fieldname":"ts_from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1
		},

		{
			"fieldname":"ts_to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1
		},

		{
			"fieldname":"ts_item_code",
			"label": __("Item Code"),
			"fieldtype": "Link",
			"width": "100",
			"options": "Item"
		}
	]
};
