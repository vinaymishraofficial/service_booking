// service_booking/service_booking/report/service_booking_summary/service_booking_summary.js

frappe.query_reports["Service Booking Summary"] = {
    "filters": [
        {
            "fieldname": "service_type",
            "label": __("Service Type"),
            "fieldtype": "Data",
            "reqd": 0
        },
        {
            "fieldname": "workflow_state",
            "label": __("Status"),
            "fieldtype": "Select",
            "options": "\nPending\nApproved\nRejected\nCompleted",
            "reqd": 0
        }
    ]
};
