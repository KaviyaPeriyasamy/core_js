import frappe
from frappe import _
from frappe.desk.form import assign_to

def validate(self,action):

	if self.status =="Converted" or self.status == "Prospect":
		self.custom_make_read_only = 1



@frappe.whitelist(allow_guest = True)
def create_todo(ref_type, ref_name, assigned_to, status, priority, description, date):
	try:
		todo = frappe.new_doc('ToDo')
		todo.description = description
		todo.reference_type = ref_type
		todo.reference_name = ref_name
		todo.assigned_by = frappe.session.user
		todo.allocated_to = assigned_to
		todo.status = status
		todo.priority = priority
		todo.date = date
		todo.save(ignore_permissions=True)
		return True
	except:
		frappe.throw(title="Error", msg=_("Todo not Created"))


@frappe.whitelist()
def create_prospect(doc):
	doc = frappe.get_doc("Lead", doc)
	
	lead_doc = frappe.copy_doc(doc)
	lead_doc.doctype = "Prospect"
	prospcet_doc = frappe.new_doc("Prospect")

	prospcet_doc.update(lead_doc.__dict__)
	if lead_doc.first_name:
		prospcet_doc.company_name = lead_doc.first_name
	if lead_doc.company_name:
		prospcet_doc.company_name = lead_doc.company_name
	if lead_doc.state2:
		prospcet_doc.state_1_= lead_doc.state2
	
	prospcet_doc.flags.ignore_mandatory = True
	prospcet_doc.save()
	prospcet_doc.append(
			"leads",
			{
				"lead": doc.name,
				
			})
	prospcet_doc.flags.ignore_mandatory = True
	prospcet_doc.save()
	if lead_doc.mobile_no:
		if not frappe.db.exists("Contact",{"mobile_no":lead_doc.mobile_no}):
			contact_doc=frappe.new_doc("Contact")
			contact_doc.first_name=lead_doc.first_name
			contact_doc.company_name=lead_doc.company_name
			contact_doc.mobile_no=lead_doc.mobile_no
			contact_doc.append(
			"links",
			{
				"link_doctype": "Prospect",
				"link_name": prospcet_doc.name
				
			})
			contact_doc.append(
			"phone_nos",
			{
				"phone": lead_doc.mobile_no,
				"is_primary_mobile_no": 1
				
			})
			contact_doc.save(ignore_permissions=True)
		else:
			contact_doc=frappe.get_doc("Contact",{"mobile_no":lead_doc.mobile_no})
			contact_doc.append(
			"links",
			{
				"link_doctype": "Prospect",
				"link_name": prospcet_doc.name
				
			})
			contact_doc.save(ignore_permissions=True)
	frappe.set_value("Lead",doc.name,"status","Prospect")
	frappe.set_value("Lead",doc.name,"custom_make_read_only",1)
	return prospcet_doc.name