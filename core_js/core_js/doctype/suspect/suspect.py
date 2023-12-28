# Copyright (c) 2023, Justsigns and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from frappe.model.mapper import get_mapped_doc

class Suspect(Document):

	def validate(self):

		if self.status in ["Prospect", "Junk"]:

			self.make_read_only = 1

@frappe.whitelist()
def create_prospect(doc):
	
	doc = frappe.get_doc("Suspect", doc)

	suspect_doc = frappe.copy_doc(doc)

	suspect_doc.doctype = "Prospect"
	suspect_doc.custom_suspect_id = doc.name
	suspect_doc.company_name = doc.company

	lead_doc = frappe.new_doc("Prospect")

	lead_doc.update(suspect_doc.__dict__)

	lead_doc.flags.ignore_mandatory = True
	lead_doc.save()

	frappe.set_value("Suspect", doc.name, "status", "Prospect")

	return lead_doc.name