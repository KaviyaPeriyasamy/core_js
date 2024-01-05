from erpnext.crm.doctype.lead.lead import Lead
import frappe
from frappe.utils import comma_and,	get_link_to_form
# core_js.core_js.utils.contact_updation.row_duplication_delete
# def row_duplication_delete():

#     contact_list = frappe.get_all("Contact", {"updated": 0}, ["name"], pluck = "name")

#     print(len(contact_list))

#     for contact in contact_list:

#         print(contact)

#         contact_doc = frappe.get_doc("Contact", contact)

#         email_list = []

#         need_to_delete_rows = []

#         for email in contact_doc.email_ids:

#             if email.email_id in email_list:
#                 need_to_delete_rows.append(email.name)
            
#             else:
#                 email_list.append(email.email_id)

#         for need_to_delete_row in need_to_delete_rows:

#             frappe.delete_doc("Contact Email", need_to_delete_row)

#         number_list = []

#         need_to_delete_rows = []

#         for number in contact_doc.phone_nos:

#             if number.phone in number_list:
#                 need_to_delete_rows.append(number.name)
            
#             else:
#                 number_list.append(number.phone)

#         for need_to_delete_row in need_to_delete_rows:

#             frappe.delete_doc("Contact Phone", need_to_delete_row)

#         frappe.db.set_value("Contact", contact_doc.name, "updated", 1)

#         frappe.db.commit()

# def merge_duplicate_contact():

#     contact_list = frappe.get_all("Contact", {"merge_updated": 0}, ["name"], pluck = "name", order_by = "creation desc")

#     print(len(contact_list))

#     for contact in contact_list:

#         print(contact)

#         if frappe.db.exists("Contact", contact):

#             contact_doc = frappe.get_doc("Contact", contact)

#             email_list = []

#             email_primary = False

#             for email in contact_doc.email_ids:

#                 email_list.append(email.email_id)

#                 if email.is_primary and not email_primary:
#                     email_primary = True

#             link_list = []

#             for link in contact_doc.links:

#                 link_list.append(link.link_name)

#             for number in contact_doc.phone_nos:

#                 duplicate_numbers = frappe.db.get_all("Contact Phone", {"parent": ["!=", contact], "phone": number.phone}, ["parent"], pluck = "parent", order_by = "creation desc")

#                 for duplicate_number in duplicate_numbers:

#                     duplicate_contact_doc = frappe.get_doc("Contact", duplicate_number)

#                     if not contact_doc.first_name:
#                         contact_doc.first_name = duplicate_contact_doc.first_name

#                     if not contact_doc.company_name:
#                         contact_doc.company_name = duplicate_contact_doc.company_name

#                     if not contact_doc.user:
#                         contact_doc.user = duplicate_contact_doc.user

#                     for email in duplicate_contact_doc.email_ids:

#                         if email.email_id not in email_list:

#                             email_list.append(email.email_id)

#                             if not email_primary:

#                                 contact_doc.append("email_ids",{
#                                     "email_id": email.email_id,
#                                     "is_primary": email.is_primary
#                                 })

#                                 if email.is_primary:
#                                     email_primary = True
                            
#                             else:
#                                 contact_doc.append("email_ids",{
#                                     "email_id": email.email_id
#                                 })

#                     for link in duplicate_contact_doc.links:

#                         if link.link_name not in link_list:

#                             link_list.append(link.link_name)

#                             contact_doc.append("links", {
#                                 "link_name": link.link_name,
#                                 "link_doctype": link.link_doctype
#                             })

#                     communication_lists = frappe.get_all("Communication Link", {"link_doctype": "Contact", "link_name": duplicate_contact_doc.name}, ["name"], pluck = "name")

#                     for communication_list in communication_lists:

#                         frappe.db.set_value("Communication Link", communication_list, "link_name", contact_doc.name)

#                     comment_list = frappe.get_all("Comment", {"comment_type": "Comment", "reference_doctype": "Contact", "reference_name": duplicate_contact_doc.name}, ["name"], pluck = "name")

#                     for comment in comment_list:
#                         frappe.db.set_value("Comment", comment, "reference_name", contact_doc.name)

#                     call_logs = frappe.get_all("Dynamic Link", {"link_doctype": "Contact", "link_name": duplicate_contact_doc.name}, ["parent"], pluck = "parent")

#                     for call_log in call_logs:
#                         frappe.db.set_value("Dynamic Link", call_log, "link_name", contact_doc.name)

#                     frappe.delete_doc("Contact", duplicate_contact_doc.name, force = 1)
                    
#             contact_doc.merge_updated = 1

#             contact_doc.db_update()

#             frappe.db.commit()

def validate(self, event):

    if frappe.flags.ignore_validate:
        return

    not_duplicate_matched = False

    phone_nos = []
    for phone in self.phone_nos:

        duplicate_number = frappe.db.get_all("Contact Phone", {"phone": phone.phone, "parent": ["!=", self.name]}, ["parent"], pluck = "parent")

        
        if duplicate_number:

            if frappe.db.exists("Contact", duplicate_number[0]):

                duplicate_doc = frappe.get_doc("Contact", duplicate_number[0])

                if self.first_name:

                    duplicate_doc.first_name = self.first_name

                for link in self.links:

                    duplicate_doc.append("links", {
                        "link_name": link.link_name,
                        "link_doctype": link.link_doctype
                    })
                
                frappe.flags.ignore_validate = True
                duplicate_doc.save()
                frappe.flags.ignore_validate = False

                link = get_link_to_form('Contact', duplicate_number[0])

                frappe.msgprint(f'Already <b>Phone Number: {phone.phone}</b> Exists, So Updated In - {format(comma_and(link))} Contact.', title = 'Message', indicator = "blue")
        else:
            phone=frappe.copy_doc(phone)
            phone.idx = len(phone_nos) + 1
            phone_nos.append(phone)
            not_duplicate_matched = True

    email_ids = []
    for email in self.email_ids:

        duplicate_email = frappe.db.get_all("Contact Email", {"email_id": email.email_id, "parent": ["!=", self.name]}, ["parent"], pluck = "parent")
        
        if duplicate_email:

            if frappe.db.exists("Contact", duplicate_email[0]):

                duplicate_doc = frappe.get_doc("Contact", duplicate_email[0])

                if self.first_name:

                    duplicate_doc.first_name = self.first_name

                for link in self.links:

                    duplicate_doc.append("links", {
                        "link_name": link.link_name,
                        "link_doctype": link.link_doctype
                    })

                frappe.flags.ignore_validate = True
                duplicate_doc.save()
                frappe.flags.ignore_validate = False

                link = get_link_to_form('Contact', duplicate_email[0])

                frappe.msgprint(f'Already <b>Email Id: {email.email_id}</b> Exists, So Updated In - {format(comma_and(link))} Contact.', title = 'Message', indicator = "blue")

        else:
            email = frappe.copy_doc(email)
            email.idx = len(email_ids) + 1
            email_ids.append(email)
            not_duplicate_matched = True

    self.update({
        'phone_nos': phone_nos,
        "email_ids": email_ids
    })

    if not not_duplicate_matched:
        self.name = None
        self.db_insert = lambda*a,**b: 1
        self.db_update = lambda*a,**b: 1
        self.run_method = lambda*a,**b: 1
        self.run_post_save_methods = lambda*a,**b: 1
        self.update_children = lambda*a,**b: 1

class _Lead(Lead):
    def before_insert(self):
        pass

    def after_insert(self):
        self.contact_doc = None
        if frappe.db.get_single_value("CRM Settings", "auto_creation_of_contact"):
            self.contact_doc = self.create_contact()
        
    def create_contact(self):
        if not self.lead_name:
            self.set_full_name()
            self.set_lead_name()

        contact = frappe.new_doc("Contact")
        contact.update(
            {
                "first_name": self.first_name or self.lead_name,
                "last_name": self.last_name,
                "salutation": self.salutation,
                "gender": self.gender,
                "job_title": self.job_title,
                "company_name": self.company_name,
            }
        )

        new_matched = False

        if self.email_id:

            duplicate_email = frappe.db.get_all("Contact Email", {"email_id": self.email_id}, ["parent"], pluck = "parent")
            
            if not duplicate_email:

                new_matched = True

                contact.append("email_ids", {"email_id": self.email_id, "is_primary": 1})
            
            else:

                duplicate_doc = frappe.get_doc("Contact", duplicate_email[0])

                duplicate_doc.append("links", {
                    "link_doctype": "Lead",
                    "link_name": self.name,
                    "link_title": self.lead_name
                })

                duplicate_doc.save()

        if self.phone:

            duplicate_number = frappe.db.get_all("Contact Phone", {"phone": self.phone}, ["parent"], pluck = "parent")

            if duplicate_number:

                duplicate_doc = frappe.get_doc("Contact", duplicate_number[0])

                duplicate_doc.append("links", {
                    "link_doctype": "Lead",
                    "link_name": self.name,
                    "link_title": self.lead_name
                })
                
                duplicate_doc.save()

            else:

                new_matched = True

                contact.append("phone_nos", {"phone": self.phone, "is_primary_phone": 1})

        if self.mobile_no:

            duplicate_number = frappe.db.get_all("Contact Phone", {"phone": self.mobile_no}, ["parent"], pluck = "parent")

            if duplicate_number:

                duplicate_doc = frappe.get_doc("Contact", duplicate_number[0])


                duplicate_doc.append("links", {
                    "link_doctype": "Lead",
                    "link_name": self.name,
                    "link_title": self.lead_name
                })
                
                duplicate_doc.save()

            else:

                new_matched = True

                contact.append("phone_nos", {"phone": self.mobile_no, "is_primary_mobile_no": 1})

        contact.append(
				"links", {"link_doctype": "Lead", "link_name": self.name, "link_title": self.lead_name}
			)
        
        if new_matched:

            contact.insert(ignore_permissions=True)
            if frappe.db.exists(contact.doctype, contact.name):
                contact.reload()  # load changes by hooks on contact

            return contact
    
# def deleting_unwanted_leads():

#     lead_list = frappe.get_all("Lead", {"status": ["in", ["Interested", "Opportunity", "Prospect"]]}, pluck = "name")

#     print(lead_list, len(lead_list))

#     for lead in lead_list:

#         print(lead)

#         parent_name_list = frappe.get_all("Dynamic Link", {"link_doctype": "Lead", "link_name": lead}, ["parent", "parenttype", "name"])

#         try:

#             for parent_name in parent_name_list:

#                 if parent_name:

#                     if parent_name["parenttype"] in ["Address", "Contact", "Call Log"]:

#                         doc = frappe.get_doc(parent_name["parenttype"], parent_name["parent"])

#                         if len(doc.links) == 1 or parent_name["parenttype"] == "Call Log":
#                             frappe.delete_doc(parent_name["parenttype"], parent_name["parent"])
                        
#                         else:
#                             frappe.delete_doc("Dynamic Link", parent_name["name"])

#             frappe.delete_doc("Lead", lead)
#             frappe.db.commit()
#         except:
#             pass
            
#  bench --site erp.justsigns.co.in execute core_js.core_js.utils.contact_updation.deleting_unwanted_leads
        
# def duplicates_mobile(doc):
#     existing_docs = frappe.get_all(
#         doc.doctype,
#         filters={
#             'phone': doc.phone,
#             'name': ['!=', doc.name],
#         },
#         fields=['name','modified'],
#         order_by="modified desc"
#     )

#     if existing_docs:
#         duplicate_names = [existing_doc["name"] for existing_doc in existing_docs]
#         print(f'Duplicate documents found with names {", ".join(duplicate_names)}. Please check mobile numbers.')
#         print(existing_docs)
#         if existing_docs[0].modified > doc.modified:
#             # frappe.delete_doc("Suspect", doc.name, ignore_permissions=True)
#             print(existing_docs[0].modified , doc.modified,"to dele",doc.name)
#         else:
#             # frappe.delete_doc("Suspect", existing_docs[0].name, ignore_permissions=True)
#             print(existing_docs[0].modified , doc.modified,"to dele",existing_docs[0].name)

# def all_sus():
#     d = frappe.get_all("Suspect",pluck="name")
#     for i in d:
#         duplicates_mobile(frappe.get_doc("Suspect",i))