# 🚀 Service Booking App for ERPNext

A powerful and intuitive **Service Booking Application** built for ERPNext that transforms how businesses manage service appointments, resource allocation, and customer bookings. Perfect for service-based organizations looking to streamline their operations and enhance customer experience.

---

## ✨ Key Features

### 📅 **Smart Booking Management**
- Create, edit, and manage service appointments with ease
- Automated booking confirmations and reminders
- Calendar integration for better scheduling visibility
- Recurring appointment support

### 👥 **Resource Allocation**
- Assign technicians, staff, or equipment to specific bookings
- Track availability and prevent double-booking
- Skill-based assignment recommendations
- Real-time resource utilization reports

### 📊 **Advanced Tracking & Analytics**
- Monitor booking statuses in real-time
- Generate comprehensive service reports
- Track customer history and preferences
- Performance metrics and KPI dashboards

### 🔐 **Security & Access Control**
- Role-based permissions using ERPNext's security framework
- Customer portal for self-service booking
- Audit trails for all booking activities
- Data encryption and privacy compliance

### 🎨 **Customization & Integration**
- Fully customizable booking forms and workflows
- Email and SMS notifications
- API integration for third-party systems
- Mobile-responsive design

---

## 🛠️ System Requirements

Before installing, ensure your system meets these requirements:

### **Core Dependencies**
- **ERPNext**: Version 14.x or 15.x
- **Frappe Framework**: Latest stable version
- **Python**: 3.8 or higher
- **Node.js**: 16.x or higher

### **Installation Tools**
- **Frappe Bench CLI**
  ```bash
  pip install frappe-bench
  ```
- **Git** (for version control)
- **MariaDB/MySQL** (database)

### **Server Requirements**
- **RAM**: Minimum 2GB (4GB recommended)
- **Storage**: At least 5GB free space
- **Network**: Stable internet connection

---

## 📥 Quick Installation

### **Step 1: Get the App**
```bash
# Navigate to your bench directory
cd ~/frappe-bench

# Clone the Service Booking app
bench get-app service_booking https://github.com/vinaymishraofficial/service_booking
```

### **Step 2: Install on Site**
```bash
# Install the app on your ERPNext site
bench --site your-site-name install-app service_booking

# Apply database migrations
bench --site your-site-name migrate
```

### **Step 3: Build and Deploy**
```bash
# Build frontend assets
bench build

# Clear cache for fresh start
bench clear-cache

# Restart the server
bench restart
```

> 💡 **Pro Tip**: Replace `your-site-name` with your actual site name (e.g., `company.local`)

---

## 🚀 Getting Started

### **1. Access the App**
After installation, log into your ERPNext dashboard:
- Look for **Service Booking** in the main menu
- Or navigate to the **Modules** section

### **2. Initial Setup**
1. **Configure Service Types**: Define your service categories
2. **Set Up Resources**: Add staff, equipment, or locations
3. **Create Booking Forms**: Customize fields as needed
4. **Configure Notifications**: Set up email/SMS alerts

### **3. First Booking**
- Navigate to **Service Booking > New**
- Fill in customer and service details
- Assign resources and set schedule
- Save and confirm the booking

---

## � Updating the App

Keep your Service Booking app up-to-date with the latest features:

```bash
# Pull latest changes
cd ~/frappe-bench/apps/service_booking
git pull origin main

# Return to bench directory
cd ~/frappe-bench

# Apply updates
bench --site your-site-name migrate
bench build
bench restart
```

---

## 🐛 Troubleshooting Guide

| **Problem** | **Solution** | **Additional Steps** |
|-------------|--------------|---------------------|
| App not visible after installation | Run migration and build | `bench migrate && bench build && bench restart` |
| Doctypes missing from menu | Clear browser cache | Use Ctrl+F5 or clear cache in browser settings |
| JavaScript/CSS not loading | Rebuild frontend assets | `bench build --force && bench restart` |
| Installation errors | Check app dependencies | Verify ERPNext version compatibility |
| Permission denied errors | Check user roles | Ensure proper role assignments in User setup |
| Database connection issues | Restart services | `bench restart && bench doctor` |

### **Advanced Debugging**
```bash
# Check system status
bench doctor

# View error logs
bench logs

# Access ERPNext console
bench --site your-site-name console

# Check app status
bench list-apps
```

---

## � Project Structure

```
service_booking/
├── 📄 README.md                    # Project documentation
├── 📄 setup.py                     # App installation script
├── 📄 hooks.py                     # ERPNext integration hooks
├── 📄 requirements.txt             # Python dependencies
├── 📁 service_booking/             # Main application module
│   ├── 📁 config/                  # App configuration files
│   ├── 📁 doctype/                 # Custom document types
│   │   └── 📁 service_booking/     # Service Booking doctype
│   │       ├── 📄 service_booking.py        # Python controller
│   │       ├── 📄 service_booking.js        # Client-side logic
│   │       ├── 📄 service_booking.json      # Document structure
│   │       └── 📄 test_service_booking.py   # Unit tests
│   ├── 📁 fixtures/                # Default data and configurations
│   ├── 📁 notification/            # Email/SMS notification templates
│   ├── 📁 print_format/            # Custom print formats
│   ├── 📁 report/                  # Custom reports and analytics
│   ├── 📁 workspace/               # Custom workspace layouts
│   └── 📁 public/                  # Static assets (CSS, JS, images)
├── 📁 patches/                     # Database migration scripts
├── 📁 templates/                   # HTML templates
└── 📁 www/                         # Web assets and pages
```

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### **How to Contribute**
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### **Contribution Guidelines**
- Follow PEP 8 coding standards for Python
- Write clear, descriptive commit messages
- Include unit tests for new features
- Update documentation as needed
- Test thoroughly before submitting

### **Areas for Contribution**
- 🐛 Bug fixes and improvements
- ✨ New features and enhancements
- 📚 Documentation updates
- 🧪 Testing and quality assurance
- 🌍 Internationalization and translations

---

## 👨‍💻 Author & Maintainer

**Vinay Mishra**  
*Full Stack Developer & ERPNext Specialist*

📧 **Email**: [vinay.alwar89@gmail.com](mailto:vinay.alwar89@gmail.com)  
🌐 **GitHub**: [github.com/vinaymishraofficial](https://github.com/vinaymishraofficial)  
🌐 **LinkedIn**: [linkedin.com/in/vinaymishraofficial](https://www.linkedin.com/in/vinaymishraofficial/)


---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### **What this means:**
- ✅ Commercial use allowed
- ✅ Modification and distribution permitted
- ✅ Private use encouraged
- ❗ Must include copyright notice
- ❗ No warranty provided

---

## 🌟 Support the Project

If this app has helped your business, consider:

- ⭐ **Star** this repository on GitHub
- 🐛 **Report** bugs and suggest features
- 💬 **Share** your experience with others
- 🤝 **Contribute** code or documentation
- ☕ **Buy me a coffee** (donation links coming soon!)

---

## 📞 Support & Community

### **Getting Help**
- 📖 Check the [Wiki](https://github.com/vinaymishraofficial/service_booking/wiki) for detailed guides
- 🐛 Report issues on [GitHub Issues](https://github.com/vinaymishraofficial/service_booking/issues)
- 💬 Join our [Community Forum](https://discuss.erpnext.com/) for discussions
- 📧 Email support: [vinay.alwar89@gmail.com](mailto:vinay.alwar89@gmail.com)

### **Community Guidelines**
- Be respectful and professional
- Search existing issues before creating new ones
- Provide detailed information when reporting bugs
- Help others in the community when possible

---

## 🔗 Related Projects

- [ERPNext](https://github.com/frappe/erpnext) - The main ERP system
- [Frappe Framework](https://github.com/frappe/frappe) - The underlying framework
- [Frappe Bench](https://github.com/frappe/bench) - Development and deployment tool

---

**Made with ❤️ for the ERPNext community**
