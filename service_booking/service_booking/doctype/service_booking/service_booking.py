import frappe
from frappe.model.document import Document

class ServiceBooking(Document):
    def on_update(self):
        if self.workflow_state == "Approved":
            recipient_email = ""

            # If it's a Link to Customer, fetch email_id
            if self.customer_name and frappe.db.exists("Customer", self.customer_name):
                recipient_email = frappe.db.get_value("Customer", self.customer_name, "email_id")

            # Or use a direct field like customer_email if present
            if not recipient_email and hasattr(self, "customer_email"):
                recipient_email = self.customer_email

            # Fallback
            if not recipient_email:
                frappe.msgprint("No email found for customer. Email not sent.")
                return

            # Send email using the template
            frappe.sendmail(
                recipients=[recipient_email],
                subject="Your Booking Has Been Approved",
                template="booking_approval" ,  # Use only the template name if it's an Email Template DocType
                args={"doc": self},
                header=["Booking Approved", "green"],
                delayed=False
            )
