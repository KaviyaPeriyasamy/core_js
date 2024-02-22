import frappe

def validate(self,action):
    if self.custom_status =="Converted":
        self.custom_make_read_only = 1

def on_trash(self,action):
    if self.custom_suspect_id:
        frappe.set_value("Suspect", self.custom_suspect_id, "status", "Open")
        frappe.set_value("Suspect", self.custom_suspect_id, "make_read_only", 0)
    for i in self.leads:
        frappe.set_value("Lead",i.lead, "status", "Interested")
        frappe.set_value("Lead", i.lead, "custom_make_read_only", 0)



def prospect_creation_script():
    customer_list=frappe.get_all("Customer",pluck="name")
    for i in customer_list:
        sale_order=frappe.get_all("Sales Order",filters={"customer":i})
        sale_invoice=frappe.get_all("Sales Invoice",filters={"customer":i})
        sales_meet=frappe.get_all("sales_meet_confirmation",filters={"customer":i})
        try:
            if not sale_order and not sale_invoice and not sales_meet:
                customer_doc=frappe.get_doc("Customer",i)
                
                if customer_doc.lead_name and customer_doc.opportunity_name:
                    prospect = frappe.new_doc("Prospect")
                    prospect.company_name=customer_doc.customer_name
                    prospect.customer_group=customer_doc.customer_group
                    prospect.samples_sent="No"
                    prospect.custom_status="New"
                    prospect.territory=customer_doc.territory
                    prospect.append(
                        "leads",
                        {
                            "lead": customer_doc.lead_name, 
                        },
                    )
                    prospect.append(
                        "opportunities",
                        {
                            "opportunity": customer_doc.opportunity_name,
                            
                        },
                    )
                    prospect.flags.ignore_permissions = True
                    prospect.flags.ignore_mandatory = True
                    prospect.save()
                    if customer_doc.customer_primary_address:
                        address_doc=frappe.get_doc("Address",customer_doc.customer_primary_address)
                        if address_doc:
                            address_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            address_doc.save(ignore_permissions=True)
                            for row in address_doc.get("links"):
        
                                if row.get("link_doctype") == "Customer":
                                    address_doc.get("links").remove(row)
                                    address_doc.save()
                    if customer_doc.customer_primary_contact:
                        contact_doc=frappe.get_doc("Contact",customer_doc.customer_primary_contact)
                        if contact_doc:
                            contact_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            contact_doc.save(ignore_permissions=True)
                            for row in contact_doc.get("links"):
        
                                if row.get("link_doctype") == "Customer":
                                    contact_doc.get("links").remove(row)
                                    contact_doc.save()
                    frappe.delete_doc("Customer",customer_doc.name)

                            
                elif customer_doc.lead_name:
                    prospect = frappe.new_doc("Prospect")
                    prospect.company_name=customer_doc.customer_name
                    prospect.customer_group=customer_doc.customer_group
                    prospect.samples_sent="No"
                    prospect.custom_status="New"
                    prospect.territory=customer_doc.territory
                    prospect.append(
                        "leads",
                        {
                            "lead": customer_doc.lead_name, 
                        },
                    )
                    prospect.flags.ignore_permissions = True
                    prospect.flags.ignore_mandatory = True
                    prospect.save()
                    if customer_doc.customer_primary_address:
                        address_doc=frappe.get_doc("Address",customer_doc.customer_primary_address)
                        if address_doc:
                            address_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            address_doc.save(ignore_permissions=True)
                            for row in address_doc.get("links"):
        
                                if row.get("link_doctype") == "Customer":
                                    address_doc.get("links").remove(row)
                                    address_doc.save()
                    if customer_doc.customer_primary_contact:
                        contact_doc=frappe.get_doc("Contact",customer_doc.customer_primary_contact)
                        if contact_doc:
                            contact_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            contact_doc.save(ignore_permissions=True)
                            for row in contact_doc.get("links"):
        
                                if row.get("link_doctype") == "Customer":
                                    contact_doc.get("links").remove(row)
                                    contact_doc.save()
                    frappe.delete_doc("Customer",customer_doc.name)

                elif customer_doc.opportunity_name:
                    prospect = frappe.new_doc("Prospect")
                    prospect.company_name=customer_doc.customer_name
                    prospect.customer_group=customer_doc.customer_group
                    prospect.samples_sent="No"
                    prospect.custom_status="New"
                    prospect.territory=customer_doc.territory
                    prospect.append(
                        "opportunities",
                        {
                            "opportunity": customer_doc.opportunity_name,
                            
                        },
                    )
                    prospect.flags.ignore_permissions = True
                    prospect.flags.ignore_mandatory = True
                    prospect.save()
                    if customer_doc.customer_primary_address:
                        address_doc=frappe.get_doc("Address",customer_doc.customer_primary_address)
                        if address_doc:
                            address_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            address_doc.save(ignore_permissions=True)
                            for row in address_doc.get("links"):
        
                                if row.get("link_doctype") == "Customer":
                                    address_doc.get("links").remove(row)
                                    address_doc.save()
                    if customer_doc.customer_primary_contact:
                        contact_doc=frappe.get_doc("Contact",customer_doc.customer_primary_contact)
                        if contact_doc:
                            contact_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            contact_doc.save(ignore_permissions=True)
                            for row in contact_doc.get("links"):
        
                                if row.get("link_doctype") == "Customer":
                                    contact_doc.get("links").remove(row)
                                    contact_doc.save()
                    frappe.delete_doc("Customer",customer_doc.name)


                elif not customer_doc.lead_name and not customer_doc.opportunity_name :
                    prospect = frappe.new_doc("Prospect")
                    prospect.company_name=customer_doc.customer_name
                    prospect.customer_group=customer_doc.customer_group
                    prospect.samples_sent="No"
                    prospect.custom_status="New"
                    prospect.territory=customer_doc.territory
                    prospect.flags.ignore_permissions = True
                    prospect.flags.ignore_mandatory = True
                    prospect.save()
                    if customer_doc.customer_primary_address:
                        address_doc=frappe.get_doc("Address",customer_doc.customer_primary_address)
                        if address_doc:
                            address_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            address_doc.save(ignore_permissions=True)
                            for row in address_doc.get("links"):
        
                                if row.get("link_doctype") == "Customer":
                                    address_doc.get("links").remove(row)
                                    address_doc.save()
                    if customer_doc.customer_primary_contact:
                        contact_doc=frappe.get_doc("Contact",customer_doc.customer_primary_contact)
                        if contact_doc:
                            contact_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            contact_doc.save(ignore_permissions=True)
                            for row in contact_doc.get("links"):
        
                                if row.get("link_doctype") == "Customer":
                                    contact_doc.get("links").remove(row)
                                    contact_doc.save()
                    frappe.delete_doc("Customer",customer_doc.name)
        except:
            print(customer_doc.name)
            pass











