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
	filters1=[
                    ["Dynamic Link", "link_doctype", "=", 'Customer'],
                   
                    ["Dynamic Link", "parenttype", "=", "Address"],
                ]
	add=frappe.get_all("Address",filters=filters1,fields=["name","state","pincode"])
	for i in add:
		add_doc=frappe.get_doc("Address",i.get("name"))
		if add_doc.pincode:
			try:
				add_doc.disabled=0
				add_doc.save()
			except Exception as e:
				
				final_data.append(i)
	
	return final_data

	