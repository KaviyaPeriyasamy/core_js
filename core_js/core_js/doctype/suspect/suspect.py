# Copyright (c) 2023, Justsigns and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from frappe.model.mapper import get_mapped_doc

class Suspect(Document):
	pass

@frappe.whitelist()
def create_lead(source_name, target_doc=None):
	# get_mapped_doc(
	# 	from_doctype = "Suspect", 
	# 	from_docname = doc_name,
	# 	{
	# 	"Payment Request": {
	# 		"doctype": "Payment Order",
	# 	}
	# 	},
	# 	target_doc = "Lead")

	return get_mapped_doc(
	"Suspect",
	source_name,
	{
		"Suspect": {
			"doctype": "Lead",
		}
	},
	target_doc
)