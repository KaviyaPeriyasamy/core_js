import frappe

def prospect_creation_script():
    customer_list=frappe.get_all("Customer",pluck="name")
    for i in customer_list:
        sale_order=frappe.get_all("Sales Order",filters={"customer":i})
        sale_invoice=frappe.get_all("Sales Invoice",filters={"customer":i})
        if not sale_order and not sale_invoice:
            customer_doc=frappe.get_doc("Customer",i)
            if customer_doc.lead_name and customer_doc.opportunity_name:
                prospect = frappe.new_doc("Prospect")
                prospect.company_name=customer_doc.customer_name
                prospect.customer_group=customer_doc.customer_group
                prospect.samples_sent="No"
                prospect.stek_status_="New"
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
                    if customer_doc.customer_primary_conatct:
                        contact_doc=frappe.get_doc("Contact",customer_doc.customer_conatct_address)
                        if contact_doc:
                            contact_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            contact_doc.save(ignore_permissions=True)
                frappe.delete_doc("Customer",customer_doc.name)

                        
            elif customer_doc.lead_name:
                prospect = frappe.new_doc("Prospect")
                prospect.company_name=customer_doc.customer_name
                prospect.customer_group=customer_doc.customer_group
                prospect.samples_sent="No"
                prospect.stek_status_="New"
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
                    if customer_doc.customer_primary_conatct:
                        contact_doc=frappe.get_doc("Contact",customer_doc.customer_conatct_address)
                        if contact_doc:
                            contact_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            contact_doc.save(ignore_permissions=True)
                frappe.delete_doc("Customer",customer_doc.name)

            else:
                prospect = frappe.new_doc("Prospect")
                prospect.company_name=customer_doc.customer_name
                prospect.customer_group=customer_doc.customer_group
                prospect.samples_sent="No"
                prospect.stek_status_="New"
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
                    if customer_doc.customer_primary_conatct:
                        contact_doc=frappe.get_doc("Contact",customer_doc.customer_conatct_address)
                        if contact_doc:
                            contact_doc.append(
                            "links",
                            {
                                "link_doctype": "Prospect",
                                "link_name": prospect.name
                                
                            })
                            contact_doc.save(ignore_permissions=True)
                frappe.delete_doc("Customer",customer_doc.name)
 