__version__ = "0.0.1"

# Optional: Add any initialization code that should run when the app loads
def get_app_info():
    """Return basic app information"""
    return {
        "app_name": "service_booking",
        "version": __version__,
        "description": "Service Booking Application for ERPNext"
    }

# Optional: Add any app-level configuration or utilities
def validate_app_dependencies():
    """Validate that required dependencies are available"""
    try:
        import frappe
        return True
    except ImportError:
        return False
