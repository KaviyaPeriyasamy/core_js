# Copyright (c) 2024, Justsigns and contributors
# For license information, please see license.txt

# import frappe


# Copyright (c) 2023, Justsigns and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = get_data()

	return columns, data

def get_columns():
	columns = [

		{
			"label": "Contact",
			"fieldtype": "Link",
			"options":"Contact",
			"fieldname": "name",
			"width": 170
		},
		
	]
	return columns


def get_data():
	final_data = []
	prospect_doc=frappe.get_all("Prospect",pluck="name")	
	
	for i in prospect_doc:
		filters1=[["Dynamic Link", "link_name", "!=", i]]
		contact=frappe.get_all("Contact",filters=filters1,fields=["name"])	
		for j in contact:
			final_data.append(j)
	
	return final_data

	
