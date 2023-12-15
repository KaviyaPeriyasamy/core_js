import frappe
from frappe import _
from frappe.desk.form import assign_to


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