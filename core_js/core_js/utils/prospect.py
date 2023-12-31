import frappe

def validate(self,action):
    if self.status =="Converted":
        self.custom_make_read_only = 1


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
                    prospect.stek_status_="New"
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

def pincode():
    w=0
    
    a=frappe.get_all("Customer",pluck="name")
    for i in a:
        filters=[
                    ["Dynamic Link", "link_doctype", "=", 'Customer'],
                    ["Dynamic Link", "link_name", "=", i],
                    ["Dynamic Link", "parenttype", "=", "Address"],
                ]
             
        address=frappe.get_all("Address",filters=filters,pluck="name")
        for j in address:
            add_doc=frappe.get_doc("Address",j)
            if len(add_doc.pincode )<6:
                w+=1
                
                
                # add_doc.pincode=result_str
                # add_doc.save(ignore_permissions=True)
                # print(add_doc.name)

        print(w)


def customer_del():
    a=frappe.get_all("Customer",{"lead_name":["is","set"],"opportunity_name":["is","not set"]},pluck="name")
    for i in a:
        sale_order=frappe.get_all("Sales Order",filters={"customer":i})
        sale_invoice=frappe.get_all("Sales Invoice",filters={"customer":i})
        sales_meet=frappe.get_all("sales_meet_confirmation",filters={"customer":i})
        try:
            if not sale_order and not sale_invoice and not sales_meet:
                filters=[
                    ["Dynamic Link", "link_doctype", "=", 'Customer'],
                    ["Dynamic Link", "link_name", "=", i],
                    ["Dynamic Link", "parenttype", "=", "Address"],
                ]
                filters1=[
                        ["Dynamic Link", "link_doctype", "=", 'Customer'],
                        ["Dynamic Link", "link_name", "=", i],
                        ["Dynamic Link", "parenttype", "=", "Contact"],
                    ]
                address=frappe.get_all("Address",filters=filters,pluck="name")
                contact=frappe.get_all("Contact",filters=filters1,pluck="name")
                for k in address:
                    address_doc=frappe.get_doc("Address",k)
                    for row in address_doc.get("links"):
                    
                        if row.get("link_doctype") == "Customer":
                            address_doc.get("links").remove(row)
                            address_doc.save()
                for u in contact:
                    contact_doc=frappe.get_doc("Contact",u)
                    for row in contact_doc.get("links"):
                    
                        if row.get("link_doctype") == "Customer":
                            contact_doc.get("links").remove(row)
                            contact_doc.save()
                frappe.delete_doc("Customer",i)
        except:
            pass

def opportunity():
    a=frappe.get_all("Opportunity",{"opportunity_from":"Customer"},pluck="name")
    for i in a:
        opp=frappe.get_doc("Opportunity",i)
        sale_order=frappe.get_all("Sales Order",filters={"customer":opp.party_name})
        sale_invoice=frappe.get_all("Sales Invoice",filters={"customer":opp.party_name})
        try:
            if not sale_order and not sale_invoice:
                if not frappe.db.exists("Prospect",opp.party_name):
                    prospect = frappe.new_doc("Prospect")
                    prospect.company_name=opp.party_name

                    prospect.samples_sent="No"
                    prospect.stek_status_="New"
                    prospect.territory=opp.territory
                    prospect.industry=opp.industry

                    
                    prospect.flags.ignore_permissions = True
                    prospect.flags.ignore_mandatory = True
                    prospect.save()
                    
                    frappe.delete_doc("Opportunity",opp.name)
        except:
            print(opp.party_name)
            pass



def test():
    a=frappe.get_all("Customer",{"lead_name":["is","set"],"opportunity_name":["is","not set"]},pluck="name")
    for i in a:
        sale_order=frappe.get_all("Sales Order",filters={"customer":i})
        sale_invoice=frappe.get_all("Sales Invoice",filters={"customer":i})
        quo=frappe.get_all("Quotation",filters={"party_name":i})
        sales_meet=frappe.get_all("sales_meet_confirmation",filters={"customer":i})
        
        try:
            if not sale_order and not sale_invoice and not sales_meet and not quo :
                opp=frappe.get_doc("Opportunity",{"opportunity_from":"Customer","party_name":i},pluck="name")
                if opp:
                    if not frappe.db.exists("Prospect",opp.party_name):
                            prospect = frappe.new_doc("Prospect")
                            prospect.company_name=opp.party_name

                            prospect.samples_sent="No"
                            prospect.stek_status_="New"
                            prospect.territory=opp.territory
                            prospect.industry=opp.industry

                            
                            prospect.flags.ignore_permissions = True
                            prospect.flags.ignore_mandatory = True
                            prospect.save()
                            
                            frappe.delete_doc("Opportunity",opp.name)
                    else:
                        frappe.delete_doc("Opportunity",opp.name)
                    frappe.delete_doc("Customer",i)
                else:

                    frappe.delete_doc("Customer",i)
        except:
            pass
            print(i)

def test1():
    sales_m=[]
    q=0
    u=0
    a=frappe.get_all("Customer",pluck="name")
    print(len(a))
    for i in a:
        sale_order=frappe.get_all("Sales Order",filters={"customer":i})
        sale_invoice=frappe.get_all("Sales Invoice",filters={"customer":i})
        sales_meet=frappe.get_all("sales_meet_confirmation",filters={"customer":i})
        delivery=frappe.get_all("Delivery Note",filters={"customer":i})
        payment=frappe.get_all("Payment Entry",filters={"party_type":"Customer","party":i})
        cus=frappe.get_doc("Customer",i)
       
        try:
            
            if not sale_order or not sale_invoice or not delivery or not payment and not sales_meet:
                
                
                if frappe.db.exists("Prospect",cus.customer_name):
                    frappe.delete_doc("Customer",i)
                    print(cus.name)
                q+=1
    
        except:
            print(cus.name)
            pass

    print(q)
            

