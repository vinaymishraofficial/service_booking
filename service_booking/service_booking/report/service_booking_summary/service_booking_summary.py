# service_booking/service_booking/report/service_booking_summary/service_booking_summary.py

import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": _("Booking ID"), "fieldname": "name", "fieldtype": "Link", "options": "Service Booking", "width": 120},
        {"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Data", "width": 150},
        {"label": _("Service Type"), "fieldname": "service_type", "fieldtype": "Data", "width": 120},
        {"label": _("Status"), "fieldname": "workflow_state", "fieldtype": "Data", "width": 100},
        {"label": _("Preferred Date"), "fieldname": "preferred_datetime", "fieldtype": "Datetime", "width": 150},
        {"label": _("Created On"), "fieldname": "creation", "fieldtype": "Datetime", "width": 150},
    ]

def get_data(filters):
    conditions = ""
    values = {}

    if filters.get("service_type"):
        conditions += " AND service_type = %(service_type)s"
        values["service_type"] = filters["service_type"]

    if filters.get("workflow_state"):
        conditions += " AND workflow_state = %(workflow_state)s"
        values["workflow_state"] = filters["workflow_state"]

    return frappe.db.sql(f"""
        SELECT
            name, customer_name, service_type, workflow_state, preferred_datetime, creation
        FROM
            `tabService Booking`
        WHERE
            1=1 {conditions}
        ORDER BY creation DESC
    """, values, as_dict=True)
