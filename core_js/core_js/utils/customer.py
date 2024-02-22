import frappe

def on_trash(doc,event):
    if doc.custom_from_prospect:
        frappe.set_value("Prospect", doc.custom_from_prospect, "status", "New")
        frappe.set_value("Prospect", doc.custom_from_prospect, "custom_make_read_only", 0)

