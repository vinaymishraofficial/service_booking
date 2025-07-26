# install.py
from service_booking.setup import setup_workspace
# This function is called before the app is installed
def before_install():
    print("Running before_install for service_booking")

# This function is called after the app is installed
def after_install():
    setup_workspace.create_default_workspace()
    print("Running after_install for service_booking")

# You can add other installation-related functions here if needed
