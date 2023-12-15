# Copyright (c) 2023, ts@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe import _
import json


def execute(filters=None):

	columns = get_columns()
	data = get_data(filters)

	return columns, data

def get_columns():
	columns = [

		{
			"label": _("Item Code"),
			"fieldtype": "Link",
			"options":"Item",
			"fieldname": "ts_item_code",
			"width": 170
		},

		{
			"label": _("Item Name"),
			"fieldtype": "Data",
			"fieldname": "ts_item_name",
			"width": 170
		},

		{
			"label": _("Open"),
			"fieldtype": "Int",
			"fieldname": "ts_open",
			"width": 80
		},

		{
			"label": _("Quotation"),
			"fieldtype": "Int",
			"fieldname": "ts_quotation",
			"width": 90
		},

		{
			"label": _("Converted"),
			"fieldtype": "Int",
			"fieldname": "ts_converted",
			"width": 90
		},

		{
			"label": _("Lost"),
			"fieldtype": "Int",
			"fieldname": "ts_lost",
			"width": 80
		},

		{
			"label": _("Replied"),
			"fieldtype": "Int",
			"fieldname": "ts_replied",
			"width": 90
		},

		{
			"label": _("Closed"),
			"fieldtype": "Int",
			"fieldname": "ts_closed",
			"width": 90
		},

		{
			"label": _("Status"),
			"fieldtype": "Data",
			"fieldname": "ts_status",
			"width": 50,
			"hidden": 1
		},

	]

	return columns

def get_data(filters):

	ts_main_data = []

	ts_filters = filters
	
	ts_opp_all = frappe.db.get_all("Opportunity", filters={"creation": ["between", (ts_filters['ts_from_date'], ts_filters['ts_to_date'])]})

	for ts_opp_name in ts_opp_all:
		ts_opp = frappe.get_doc("Opportunity", ts_opp_name)

		if not ts_main_data:
			
			for ts_item in ts_opp.items:
				
				try:
					if ts_filters["ts_item_code"] == ts_item.item_code:
						ts_sub_data = frappe._dict()

						ts_sub_data["ts_item_code"] = ts_item.item_code
						ts_sub_data["ts_item_name"] = ts_item.item_name
						ts_sub_data["ts_status"] = ts_opp.status

						if ts_opp.status == "Open":
							ts_sub_data["ts_open"] = 1

						elif ts_opp.status == "Quotation":
							ts_sub_data["ts_quotation"] = 1

						elif ts_opp.status == "Converted":
							ts_sub_data["ts_converted"] = 1

						elif ts_opp.status == "Lost":
							ts_sub_data["ts_lost"] = 1

						elif ts_opp.status == "Replied":
							ts_sub_data["ts_replied"] = 1

						elif ts_opp.status == "Closed":
							ts_sub_data["ts_closed"] = 1
					
						if ts_sub_data:
							ts_main_data.append(ts_sub_data)

				except:

					ts_sub_data = frappe._dict()

					ts_sub_data["ts_item_code"] = ts_item.item_code
					ts_sub_data["ts_item_name"] = ts_item.item_name
					ts_sub_data["ts_status"] = ts_opp.status

					if ts_opp.status == "Open":
						ts_sub_data["ts_open"] = 1

					elif ts_opp.status == "Quotation":
						ts_sub_data["ts_quotation"] = 1

					elif ts_opp.status == "Converted":
						ts_sub_data["ts_converted"] = 1

					elif ts_opp.status == "Lost":
						ts_sub_data["ts_lost"] = 1

					elif ts_opp.status == "Replied":
						ts_sub_data["ts_replied"] = 1

					elif ts_opp.status == "Closed":
						ts_sub_data["ts_closed"] = 1
				
					if ts_sub_data:
						ts_main_data.append(ts_sub_data)

		else:
			frappe.errprint(ts_main_data)
			
			for ts_item in ts_opp.items:

				try:
					if ts_filters["ts_item_code"] == ts_item.item_code:
						ts_sub_data = frappe._dict()

						ts_is_mapped = False

						for ts_main in ts_main_data:
							if ts_main["ts_item_code"] == ts_item.item_code and ts_main["ts_status"] == ts_opp.status:
								
								ts_is_mapped = True

								if ts_opp.status == "Open":
									ts_main["ts_open"] += 1

								elif ts_opp.status == "Quotation":
									ts_main["ts_quotation"] += 1

								elif ts_opp.status == "Converted":
									ts_main["ts_converted"] += 1

								elif ts_opp.status == "Lost":
									ts_main["ts_lost"] += 1

								elif ts_opp.status == "Replied":
									ts_main["ts_replied"] += 1

								elif ts_opp.status == "Closed":
									ts_main["ts_closed"] += 1

						if not ts_is_mapped:
							ts_sub_data["ts_item_code"] = ts_item.item_code
							ts_sub_data["ts_item_name"] = ts_item.item_name
							ts_sub_data["ts_status"] = ts_opp.status

							if ts_opp.status == "Open":
								ts_sub_data["ts_open"] = 1

							elif ts_opp.status == "Quotation":
								ts_sub_data["ts_quotation"] = 1

							elif ts_opp.status == "Converted":
								ts_sub_data["ts_converted"] = 1

							elif ts_opp.status == "Lost":
								ts_sub_data["ts_lost"] = 1

							elif ts_opp.status == "Replied":
								ts_sub_data["ts_replied"] = 1

							elif ts_opp.status == "Closed":
								ts_sub_data["ts_closed"] = 1

						if ts_sub_data:
							ts_main_data.append(ts_sub_data)
						
				except:

					ts_sub_data = frappe._dict()

					ts_is_mapped = False

					for ts_main in ts_main_data:
						if ts_main["ts_item_code"] == ts_item.item_code and ts_main["ts_status"] == ts_opp.status:
							
							ts_is_mapped = True

							if ts_opp.status == "Open":
								ts_main["ts_open"] += 1

							elif ts_opp.status == "Quotation":
								ts_main["ts_quotation"] += 1

							elif ts_opp.status == "Converted":
								ts_main["ts_converted"] += 1

							elif ts_opp.status == "Lost":
								ts_main["ts_lost"] += 1

							elif ts_opp.status == "Replied":
								ts_main["ts_replied"] += 1

							elif ts_opp.status == "Closed":
								ts_main["ts_closed"] += 1

					if not ts_is_mapped:
						ts_sub_data["ts_item_code"] = ts_item.item_code
						ts_sub_data["ts_item_name"] = ts_item.item_name
						ts_sub_data["ts_status"] = ts_opp.status

						if ts_opp.status == "Open":
							ts_sub_data["ts_open"] = 1

						elif ts_opp.status == "Quotation":
							ts_sub_data["ts_quotation"] = 1

						elif ts_opp.status == "Converted":
							ts_sub_data["ts_converted"] = 1

						elif ts_opp.status == "Lost":
							ts_sub_data["ts_lost"] = 1

						elif ts_opp.status == "Replied":
							ts_sub_data["ts_replied"] = 1

						elif ts_opp.status == "Closed":
							ts_sub_data["ts_closed"] = 1

					if ts_sub_data:
						ts_main_data.append(ts_sub_data)

	return ts_main_data


	

			
			
			
			

