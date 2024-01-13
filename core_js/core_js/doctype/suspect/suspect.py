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

	lead_doc = frappe.new_doc("Prospect")

	lead_doc.update(suspect_doc.__dict__)
	if suspect_doc.first_name:
		lead_doc.company_name = suspect_doc.first_name
	if suspect_doc.company_name:
		lead_doc.company_name = suspect_doc.company_name
	if suspect_doc.lead_name:
		lead_doc.company_name = suspect_doc.lead_name
	
	lead_doc.flags.ignore_mandatory = True
	lead_doc.save()
	if suspect_doc.mobile_no:
		if not frappe.db.exists("Contact",{"mobile_no":suspect_doc.mobile_no}):
			contact_doc=frappe.new_doc("Contact")
			contact_doc.first_name=suspect_doc.first_name
			contact_doc.company_name=suspect_doc.company_name
			contact_doc.mobile_no=suspect_doc.mobile_no
			contact_doc.append(
			"links",
			{
				"link_doctype": "Prospect",
				"link_name": lead_doc.name
				
			})
			contact_doc.append(
			"phone_nos",
			{
				"phone": suspect_doc.mobile_no,
				"is_primary_mobile_no": 1
				
			})
			contact_doc.save(ignore_permissions=True)
		else:
			contact_doc=frappe.get_doc("Contact",{"mobile_no":suspect_doc.mobile_no})
			contact_doc.append(
			"links",
			{
				"link_doctype": "Prospect",
				"link_name": lead_doc.name
				
			})
			contact_doc.save(ignore_permissions=True)

	frappe.set_value("Suspect", doc.name, "status", "Prospect")

	return lead_doc.name





def create_contact():
	prospect_doc=frappe.get_all("Prospect",{"custom_suspect_id":["is","set"]},pluck="name")
	for i in prospect_doc:
		prospect_doc=frappe.get_doc("Prospect",i)
		suspect_doc=frappe.get_doc("Suspect",prospect_doc.custom_suspect_id)

		if suspect_doc and suspect_doc.mobile_no:
			if not frappe.db.exists("Contact",{"mobile_no":suspect_doc.mobile_no}):

				contact_doc=frappe.new_doc("Contact")
				contact_doc.first_name=suspect_doc.first_name
				contact_doc.company_name=suspect_doc.company_name
				contact_doc.mobile_no=suspect_doc.mobile_no
				contact_doc.append(
				"links",
				{
					"link_doctype": "Prospect",
					"link_name": i
					
				})
				contact_doc.append(
				"phone_nos",
				{
					"phone": suspect_doc.mobile_no,
					"is_primary_mobile_no": 1
					
				})
				contact_doc.save(ignore_permissions=True)
			else:
				contact_doc=frappe.get_doc("Contact",{"mobile_no":suspect_doc.mobile_no})
				contact_doc.append(
				"links",
				{
					"link_doctype": "Prospect",
					"link_name": i
					
				})
				contact_doc.save(ignore_permissions=True)

