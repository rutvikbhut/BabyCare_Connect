# BabyCare Connect - Quick Reference Guide

## Quick Start (60 seconds)

```bash
# 1. Navigate to project
cd d:\Intership PY\Project\BabyCare_Connect

# 2. Activate virtual environment
.venv\Scripts\activate

# 3. Run server
python manage.py runserver

# 4. Open browser
http://127.0.0.1:8000/
```

---

## Test Accounts

### Parent User
- **Email:** parent@test.com
- **Password:** password123
- **Role:** Parent (Looking for care)

### Provider User
- **Email:** provider@test.com
- **Password:** password123
- **Role:** Provider (Offering care)

### Admin User
- **Email:** admin@test.com
- **Password:** admin123
- **Access:** Admin Dashboard & Django Admin

*Create these via registration form or Django admin panel*

---

## Key URLs

| Page | URL | For Whom |
|------|-----|----------|
| Home | `/` | Everyone |
| Register | `/register/` | New users |
| Login | `/login/` | Users |
| Services | `/service_list/` | Parents |
| Service Details | `/service_detail/<id>/` | Parents |
| My Bookings | `/parent_bookings/` | Parents |
| Dashboard | `/provider_dashboard/` | Providers |
| Add Service | `/add_service/` | Providers |
| Manage Dates | `/manage_availability/<id>/` | Providers |
| Admin Panel | `/admin_dashboard/` | Admins |
| Messages | `/inbox/` | All users |
| Chat | `/chat_room/<user_id>/` | All users |
| Django Admin | `/admin/` | Superuser |

---

## Common Commands

### Database
```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database
python manage.py flush

# Create superuser
python manage.py createsuperuser

# Access database shell
python manage.py dbshell

# Export data
python manage.py dumpdata > backup.json

# Import data
python manage.py loaddata backup.json
```

### Server
```bash
# Start development server
python manage.py runserver

# Run with specific port
python manage.py runserver 8080

# Run as public
python manage.py runserver 0.0.0.0:8000
```

### Python Shell
```bash
# Open interactive shell
python manage.py shell

# Common operations
from django.contrib.auth.models import User
from babycareapp.models import Booking, Service

# List all users
User.objects.all()

# Get specific user
User.objects.get(email='test@example.com')

# Count records
User.objects.count()
Booking.objects.filter(status='paid').count()
```

### Utilities
```bash
# Collect static files
python manage.py collectstatic

# Create cache table
python manage.py createcachetable

# Run tests
python manage.py test

# Check for issues
python manage.py check

# Show migrations
python manage.py showmigrations
```

---

## File Locations

- **Main Views:** `babycare/babycareapp/views.py`
- **Models:** `babycare/babycareapp/models.py`
- **Templates:** `babycare/babycareapp/templates/babycareapp/`
- **Static Files:** `babycare/babycareapp/static/`
- **Database:** `babycare/db.sqlite3`
- **Settings:** `babycare/babycare/settings.py`
- **URLs:** `babycare/babycare/urls.py` & `babycare/babycareapp/urls.py`

---

## User Workflows at a Glance

### Parent Books a Service
```
1. Register → 2. Login → 3. Search Services → 4. View Details → 5. Book Now
→ 6. Wait for confirmation → 7. Payment → 8. Download Invoice
```

### Provider Offers Service
```
1. Register as Provider → 2. Add Service → 3. Set Availability → 4. Wait for Bookings
→ 5. Confirm Booking → 6. Receive Payment → 7. Send Invoice
```

### Admin Monitors Platform
```
1. Login as Admin → 2. View Dashboard → 3. Check Statistics → 4. Manage Users/Services
→ 5. Monitor Finances
```

---

## Status Flow

### Booking Status
```
Pending (Parent booked) 
  ↓
Confirmed (Provider approved) 
  ↓
Paid (Payment received) 
  ↓
Completed
```

### Service Status
```
Available (is_available=True)
  ↓
Has Availability Blocks (specific dates)
```

---

## Key Features

✅ **User Management**
- 3 roles: Parent, Provider, Admin
- Email validation
- Password hashing
- Login/Logout

✅ **Service Management**
- Add/Edit services
- Hourly rate pricing
- Location-based search
- Service images

✅ **Booking System**
- Request bookings
- Confirm/Reject
- Track status
- Payment tracking

✅ **Availability**
- Block unavailable dates
- Prevent past date blocking

✅ **Messaging**
- Chat between users
- Unread message tracking
- Typing indicators

✅ **Invoicing**
- Generate PDF receipts
- Email invoices
- Download receipts

✅ **Analytics**
- Admin dashboard
- Platform statistics
- Top services
- Revenue tracking (10% commission)

---

## Validation Rules

### Email
- Must be valid email format
- Must be unique in system

### Password
- Minimum 6 characters
- Case-sensitive

### Service Title
- Minimum 3 characters

### Service Location
- Minimum 3 characters

### Hourly Rate
- Must be numeric
- Must be greater than 0

### Contact Message
- Minimum 10 characters

### Availability Dates
- Cannot be in the past
- Format: YYYY-MM-DD

---

## Commission Structure

```
Parent pays: $100
Provider receives: $90 (90%)
Platform keeps: $10 (10% commission)
```

Example in dashboard:
- **Service Rate:** $25/hour
- **Net Pay:** $22.50 (90% after commission)

---

## Email Notifications

Sent to:

**Parent:**
- ✉️ Welcome email (registration)
- ✉️ Contact form confirmation
- ✉️ Invoice receipt (after payment)

**Provider:**
- ✉️ Welcome email (registration)
- Email sent to parent when payment confirmed

**Admin:**
- (No automated emails currently)

---

## Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| Server won't start | `pip install -r requirements.txt` then `python manage.py migrate` |
| 404 on pages | Check URLs in `urls.py` files |
| Database locked | `del db.sqlite3` then `python manage.py migrate` |
| Static files missing | `python manage.py collectstatic` |
| Email not working | Check settings.py EMAIL configuration |
| Login fails | Ensure user exists and password is correct |
| Booking fails | Check service is_available=True |

---

## Development Settings

```python
# settings.py for development
DEBUG = True
ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

## Production Settings

```python
# settings.py for production
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## Database Schema Overview

```
User
  ├─ Standard Django User fields
  └─ role (parent/provider/admin)

Service
  ├─ provider (FK to User)
  ├─ title, description
  ├─ hourly_rate
  ├─ location
  ├─ image
  └─ is_available

Booking
  ├─ parent (FK to User)
  ├─ service (FK to Service)
  ├─ start_date
  ├─ status (pending/confirmed/paid)
  └─ timestamp

Message
  ├─ sender (FK to User)
  ├─ receiver (FK to User)
  ├─ content
  ├─ is_read
  └─ timestamp

Availability
  ├─ service (FK to Service)
  └─ date

contact
  ├─ name, email
  ├─ subject, message
  └─ timestamp
```

---

## Performance Tips

1. **Add indexes to common search fields**
   ```python
   # models.py
   class Service(models.Model):
       location = models.CharField(db_index=True)
   ```

2. **Use select_related for foreign keys**
   ```python
   Booking.objects.select_related('parent', 'service')
   ```

3. **Cache frequently accessed data**
   ```python
   from django.views.decorators.cache import cache_page
   @cache_page(60 * 15)  # Cache for 15 minutes
   def service_list(request): ...
   ```

---

## Environment Variables (for production)

Create `.env` file:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

Then in settings.py:
```python
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
```

---

## Next Steps for Enhancement

📋 Potential Improvements:
- [ ] Add rating system (parents rate providers)
- [ ] Add review system
- [ ] Add payment gateway integration (Stripe/PayPal)
- [ ] Add real-time notifications (WebSockets)
- [ ] Add background task queue (Celery)
- [ ] Add search filters (rating, price, availability)
- [ ] Add service cancellation policy
- [ ] Add escrow payment system
- [ ] Add dispute resolution
- [ ] Add activity logs

---

**Happy Coding! 🎉**

For full documentation, see: `PROJECT_GUIDE.md`
