def after_install():
    from service_booking.setup.setup_dashboard import create_dashboard
    from service_booking.setup.setup_roles import create_roles
    from service_booking.setup.setup_workspace import create_workspace

    create_roles()
    create_dashboard()
    create_workspace()
