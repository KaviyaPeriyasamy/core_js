# Copyright (c) 2023, Justsigns and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from frappe.model.mapper import get_mapped_doc

class Suspect(Document):
	def on_update(self):

		if self.status in ["Lead", "Junk"] and self.docstatus == 0:

			self.submit()

@frappe.whitelist()
def create_lead(doc):
	frappe.errprint(doc)
	doc = frappe.get_doc("Suspect", doc)



	suspect_doc = frappe.copy_doc(doc)

	suspect_doc.doctype = "Lead"
	suspect_doc.custom_suspect_id = doc.name

	lead_doc = frappe.new_doc("Lead")

	lead_doc.update(suspect_doc.__dict__)

	lead_doc.save()

	frappe.set_value("Suspect", doc.name, "status", "Lead")

	return lead_doc.name