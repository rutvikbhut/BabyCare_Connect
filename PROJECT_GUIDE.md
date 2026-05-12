# BabyCare Connect - Project Management & Usage Guide

## Table of Contents
1. [Initial Setup](#initial-setup)
2. [Running the Project](#running-the-project)
3. [User Roles & Features](#user-roles--features)
4. [How to Use](#how-to-use)
5. [Admin Management](#admin-management)
6. [Troubleshooting](#troubleshooting)

---

## Initial Setup

### 1. Install Dependencies
```bash
# Navigate to project directory
cd d:\Intership PY\Project\BabyCare_Connect

# Activate virtual environment
.venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Database Setup
```bash
# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
```

### 3. Static Files
```bash
python manage.py collectstatic --noinput
```

---

## Running the Project

### Start Development Server
```bash
# Activate environment first
.venv\Scripts\activate

# Run server
python manage.py runserver
```

**Access the application:**
- **Frontend:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

---

## User Roles & Features

### 1. **PARENT (Default User)**
**Purpose:** Looking for childcare services

**Features:**
- ✅ Register/Login
- ✅ Search services by location
- ✅ View service details
- ✅ Book services (create bookings)
- ✅ View my bookings
- ✅ Download invoices (after payment)
- ✅ Chat with providers
- ✅ View booking status
- ✅ Contact support

**URL Access:**
- Service List: `/service_list/`
- My Bookings: `/parent_bookings/`
- Messages: `/inbox/`

---

### 2. **PROVIDER (Service Provider)**
**Purpose:** Offer childcare services

**Features:**
- ✅ Register as Provider
- ✅ Add childcare services
- ✅ Manage service availability
- ✅ View incoming booking requests
- ✅ Confirm/Reject bookings
- ✅ Mark payments as paid
- ✅ View earnings & monthly reports
- ✅ Chat with parents
- ✅ Send invoices via email

**URL Access:**
- Dashboard: `/provider_dashboard/`
- Add Service: `/add_service/`
- Manage Availability: `/manage_availability/<service_id>/`
- Inbox: `/inbox/`

---

### 3. **ADMIN (Platform Manager)**
**Purpose:** Manage entire platform

**Features:**
- ✅ View all users (parents, providers, admins)
- ✅ View all bookings & their status
- ✅ Monitor platform finances
- ✅ View top services
- ✅ Track commission earnings
- ✅ View detailed statistics

**URL Access:**
- Admin Dashboard: `/admin_dashboard/`
- Django Admin: `/admin/` (Superuser only)

---

## How to Use

### **PARENT WORKFLOW**

#### Step 1: Register
1. Go to http://127.0.0.1:8000/
2. Click "Register"
3. Fill form:
   - Name
   - Email
   - Password (min 6 chars)
   - Confirm Password
   - Select: **"Parent (Looking for care)"**
   - Agree to Terms ✓
4. Click "Register"
5. Login with your email & password

#### Step 2: Search Services
1. Go to "Services" menu
2. Enter location (city/area) in search box
3. Browse available services
4. Click "View Details" for more info

#### Step 3: Book a Service
1. Click "Book Now" on any service
2. Booking created with status: **"Pending"**
3. Wait for provider to confirm
4. You'll receive email notification

#### Step 4: Check Booking Status
1. Go to "My Bookings"
2. View status of each booking:
   - **Pending:** Waiting for provider approval
   - **Confirmed:** Provider approved
   - **Paid:** Payment complete (can download invoice)

#### Step 5: Download Invoice
1. Go to "My Bookings"
2. Find **"Paid"** booking
3. Click "Download Receipt"
4. PDF will download

#### Step 6: Chat with Provider
1. Go to "Messages" (inbox)
2. Click provider name to start chat
3. Type message and send
4. You'll see typing indicators & message status (✓ sent, ✓✓ read)

---

### **PROVIDER WORKFLOW**

#### Step 1: Register as Provider
1. Go to http://127.0.0.1:8000/
2. Click "Register"
3. Fill form (same as parent)
4. Select: **"Provider (Offering care)"**
5. Login

#### Step 2: Add a Service
1. From dashboard, click "Add Service"
2. Fill details:
   - **Service Title:** (e.g., "Morning Nanny Service")
   - **Description:** (Optional)
   - **Hourly Rate:** (e.g., 25.00)
   - **Location:** (e.g., "New York, NY")
   - **Photo:** (Optional)
3. Click "Create Listing"
4. Service visible to parents

#### Step 3: Manage Availability
1. Go to dashboard
2. Find your service
3. Click "Manage Availability"
4. Select dates when you're **NOT available**
5. Click "Block Date"
6. Parents won't see these dates

#### Step 4: Process Bookings
1. Go to **Provider Dashboard**
2. View all booking requests
3. For each booking:
   - **Confirm:** Parent's booking is approved
   - **Reject:** Decline the booking
4. Status updates to "**Confirmed**"

#### Step 5: Receive Payment
1. Parent pays (via your payment system)
2. Click "**Confirm Payment**"
3. Invoice sent to parent email
4. You earn 90% (10% platform commission)

#### Step 6: View Earnings
1. Dashboard shows:
   - **Total Earnings** from paid bookings
   - **Monthly Report** breakdown
   - **Net Pay** (90% after commission)

#### Step 7: Chat with Parents
1. Go to "Messages"
2. Click parent name
3. Send/receive messages
4. Typing indicator shows when parent is typing

---

### **ADMIN WORKFLOW**

#### Access Admin Dashboard
1. URL: http://127.0.0.1:8000/admin_dashboard/
2. Must be admin user (role='admin')

#### View Statistics
- **Users:** Total parents, providers, admins
- **Bookings:** Pending, confirmed, paid counts
- **Revenue:** Total platform earnings (commissions)
- **Top Services:** Most popular services
- **Profit:** Platform earnings (10% commission)

#### Manage via Django Admin
1. URL: http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Manage:
   - Users (create, edit, delete)
   - Services
   - Bookings
   - Messages
   - Contact submissions

---

## Admin Management

### Creating Users via Command Line
```bash
# Create parent user
python manage.py createsuperuser

# Or use shell
python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user(
...     username='john@example.com',
...     email='john@example.com',
...     password='password123',
...     first_name='John'
... )
>>> user.role = 'parent'
>>> user.save()
```

### Database Management
```bash
# View database tables
python manage.py dbshell

# Backup database
# Copy: db.sqlite3 to safe location

# Reset database (WARNING: deletes all data)
python manage.py flush
python manage.py migrate
```

### Clear Cache/Temporary Files
```bash
# Remove temporary files
python manage.py cleanup

# Clear old uploads
python manage.py clean_files
```

---

## Project Structure

```
babycare/
├── manage.py                 # Django management
├── db.sqlite3               # Database file
├── babycare/
│   ├── settings.py          # Configuration
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI config
│   └── asgi.py              # ASGI config
├── babycareapp/
│   ├── models.py            # Database models
│   ├── views.py             # View logic (FIXED)
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin panel config
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates (FIXED)
│   ├── static/              # CSS, JS, images
│   └── urls.py              # App URLs
├── media/                   # User uploads
├── static/                  # Global static files
└── .venv/                   # Virtual environment
```

---

## Features Overview

| Feature | Parent | Provider | Admin |
|---------|--------|----------|-------|
| Register/Login | ✅ | ✅ | ✅ |
| Search Services | ✅ | ❌ | ❌ |
| Book Services | ✅ | ❌ | ❌ |
| Add Services | ❌ | ✅ | ❌ |
| Manage Availability | ❌ | ✅ | ❌ |
| Process Bookings | ❌ | ✅ | ❌ |
| Download Invoice | ✅ | ❌ | ❌ |
| Send Invoice Email | ❌ | ✅ | ❌ |
| Chat/Messaging | ✅ | ✅ | ❌ |
| Contact Support | ✅ | ✅ | ✅ |
| View Dashboard | ❌ | ✅ | ✅ |
| View All Users | ❌ | ❌ | ✅ |
| Monitor Finances | ❌ | ❌ | ✅ |

---

## Common Tasks

### Reset User Password
```bash
python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(email='user@example.com')
>>> user.set_password('newpassword123')
>>> user.save()
```

### Check Pending Bookings
```bash
python manage.py shell
>>> from babycareapp.models import Booking
>>> Booking.objects.filter(status='pending')
```

### Create Test Admin User
```bash
python manage.py createsuperuser
# Username: admin
# Email: admin@test.com
# Password: admin123
```

### Export Data
```bash
# Export users
python manage.py dumpdata auth.User > users.json

# Export all data
python manage.py dumpdata > backup.json
```

---

## Troubleshooting

### Issue: Server won't start
```bash
# Check Python version
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Migrate database
python manage.py migrate
```

### Issue: Static files not loading
```bash
python manage.py collectstatic --noinput
```

### Issue: Database locked/corrupted
```bash
# Backup old database
copy db.sqlite3 db.sqlite3.backup

# Create new database
del db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Issue: Email not sending
- Check email settings in `settings.py`
- Verify SMTP credentials
- Gmail requires "App Password" not regular password

### Issue: File uploads not working
```bash
# Create media directory
mkdir media

# Check permissions
# Ensure directory is writable
```

---

## Security Notes

⚠️ **Before Deployment:**
1. Change `DEBUG = False` in settings.py
2. Set strong `SECRET_KEY`
3. Add domain to `ALLOWED_HOSTS`
4. Use environment variables for sensitive data
5. Enable HTTPS
6. Set up proper email backend
7. Backup database regularly

---

## Email Configuration

### Gmail Setup
```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Not regular password!
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

### Local Testing (No Email)
```python
# settings.py - for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Emails print to console instead
```

---

## Performance Tips

1. **Database:**
   - Use `.select_related()` for foreign keys
   - Use `.prefetch_related()` for many-to-many
   - Index frequently searched fields

2. **Caching:**
   - Cache service listings
   - Cache user dashboard data

3. **Images:**
   - Compress service photos
   - Use CDN for media files

4. **Queries:**
   - Avoid N+1 query problems
   - Use `.only()` and `.defer()`

---

## Support & Help

### View Logs
```bash
# Check Django logs
python manage.py runserver 2>&1 | tee server.log
```

### Debug Mode
```python
# settings.py
DEBUG = True  # Show detailed error pages
```

### Email Test
```bash
python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Test', 'Hello', 'from@example.com', ['to@example.com'])
```

---

## Summary

**BabyCare Connect** is a complete childcare booking platform with:
- ✅ **Parents** can find and book services
- ✅ **Providers** can offer services and manage bookings
- ✅ **Admins** can monitor platform statistics
- ✅ **Messaging** system for communication
- ✅ **Payment** tracking and invoices
- ✅ **Email** notifications

**All features are now fixed and working properly!** 🎉
