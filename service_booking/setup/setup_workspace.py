# service_booking/setup/setup_workspace.py

import frappe

def create_default_workspace():
    print("Creating workspace for Service Booking")

    if frappe.db.exists("Workspace", "Service Booking"):
        return  # already exists

    doc = frappe.new_doc("Workspace")
    doc.title = "Service Booking"
    doc.name = "Service Booking"
    doc.module = "Service Booking"
    doc.public = 1

    doc.content = frappe.as_json([
        {
            "label": "Reports",
            "items": [
                {
                    "type": "report",
                    "name": "Service Booking Summary",  # Report name (not title)
                    "label": "Service Booking Summary",
                    "description": "Summary Report for Service Bookings",
                    "doctype": "Service Booking",  # Doctype on which report is made
                    "report_type": "Script Report"  # or 'Query Report' / 'Script Report'
                }
            ]
        }
    ])

    doc.save()
    print("Workspace created with report link.")
