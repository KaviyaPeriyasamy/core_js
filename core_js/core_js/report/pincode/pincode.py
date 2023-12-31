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
			"label": "Address",
			"fieldtype": "Link",
			"options":"Address",
			"fieldname": "name",
			"width": 170
		},
		{
			"label": "State",
			"fieldtype": "Data",
			
			"fieldname": "state",
			"width": 170
		},
		{
			"label": "Pincode",
			"fieldtype": "Data",
			
			"fieldname": "pincode",
			"width": 170
		},
	]
	return columns


def get_data():
	final_data = []
	add=frappe.get_all("Address",fields=["name","state","pincode"])
	for i in add:
		add_doc=frappe.get_doc("Address",i.get("name"))
		if add_doc.pincode:
			if len(add_doc.pincode)<6 :
				final_data.append(i)
	frappe.errprint(final_data)
	return final_data

	