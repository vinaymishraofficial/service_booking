import frappe

def execute():
    if not frappe.db.exists("Role", "Service Manager"):
        frappe.get_doc({
            "doctype": "Role",
            "role_name": "Service Manager",
            "desk_access": 1
        }).insert()
        frappe.db.commit()
