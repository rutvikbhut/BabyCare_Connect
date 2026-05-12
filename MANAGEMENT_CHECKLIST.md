# BabyCare Connect - Management Checklist

## Daily Operations

### Morning Checklist
- [ ] Start Django server: `python manage.py runserver`
- [ ] Check server logs for errors
- [ ] Verify database is accessible
- [ ] Test email notifications are working
- [ ] Check for pending operational issues

### During Operation
- [ ] Monitor new user registrations
- [ ] Check for pending bookings (provider confirmations)
- [ ] Verify payments are being processed
- [ ] Monitor chat/messaging system
- [ ] Check for contact form submissions

### Evening Checklist
- [ ] Review daily activity statistics
- [ ] Backup database (`copy db.sqlite3 db.sqlite3.backup`)
- [ ] Check error logs
- [ ] Verify all services are still functional
- [ ] Stop server gracefully (Ctrl+C)

---

## Weekly Management Tasks

### User Management
- [ ] Monitor user registrations
- [ ] Check for suspended/inactive accounts
- [ ] Review user complaints/support requests
- [ ] Verify email delivery rates
- [ ] Check password reset requests

### Service Management
- [ ] Review newly added services
- [ ] Check for service quality/compliance
- [ ] Monitor service ratings (future feature)
- [ ] Remove inappropriate services
- [ ] Update service recommendations

### Financial Management
- [ ] Calculate platform commission earned
- [ ] Verify all paid bookings
- [ ] Check payment processing
- [ ] Generate financial reports
- [ ] Review earnings by provider

### Technical Maintenance
- [ ] Check database size
- [ ] Verify backup integrity
- [ ] Review error logs
- [ ] Test all major features
- [ ] Check static file delivery

### Communication
- [ ] Review contact form submissions
- [ ] Respond to support inquiries
- [ ] Send platform announcements
- [ ] Monitor chat quality
- [ ] Address user complaints

---

## Monthly Management Tasks

### Strategic Review
- [ ] Generate monthly report
- [ ] Analyze user growth trends
- [ ] Calculate monthly revenue
- [ ] Review service popularity
- [ ] Plan improvements

### System Maintenance
- [ ] Full database backup & archive
- [ ] Clean old temporary files
- [ ] Review and optimize database queries
- [ ] Update dependencies
- [ ] Security audit

### User Analytics
- [ ] Parent retention rate
- [ ] Provider satisfaction
- [ ] Booking completion rate
- [ ] Average rating (future)
- [ ] User acquisition cost

### Financial Reconciliation
- [ ] Verify all payments processed
- [ ] Calculate provider payouts
- [ ] Generate P&L statement
- [ ] Review payment disputes
- [ ] Plan budget for next month

### Quality Assurance
- [ ] Test all features
- [ ] Verify email delivery
- [ ] Check PDF generation
- [ ] Test payment flow
- [ ] User experience review

---

## Monthly Dashboard Report Template

```
BABENCYCARE CONNECT – MONTHLY REPORT

Month: ____________

USERS
- New Parents: ___
- New Providers: ___
- Total Active Users: ___
- New Admins: ___

SERVICES
- Total Services: ___
- New Services Added: ___
- Top 5 Services: _______________
- Inactive Services: ___

BOOKINGS
- Total Bookings: ___
- Pending: ___
- Confirmed: ___
- Paid: ___
- Completion Rate: ___%
- Average Booking Value: $___

FINANCES
- Total Revenue (All Bookings): $___
- Platform Commission (10%): $___
- Provider Payouts (90%): $___
- Net Platform Profit: $___

MESSAGING
- Total Messages: ___
- Active Conversations: ___
- Average Response Time: ___ hours

SUPPORT
- Contact Form Submissions: ___
- Support Tickets Resolved: ___
- Average Resolution Time: ___ hours
- User Satisfaction: ___%

TECHNICAL
- Server Uptime: ___%
- Database Size: ___ MB
- Backup Status: ✓ / ✗
- Errors This Month: ___
```

---

## Admin Dashboard Commands

### Quick Stats Check
```bash
python manage.py shell

# Total users by role
from django.contrib.auth.models import User
print("Parents:", User.objects.filter(role='parent').count())
print("Providers:", User.objects.filter(role='provider').count())
print("Admins:", User.objects.filter(role='admin').count())

# Booking summary
from babycareapp.models import Booking
print("Pending:", Booking.objects.filter(status='pending').count())
print("Confirmed:", Booking.objects.filter(status='confirmed').count())
print("Paid:", Booking.objects.filter(status='paid').count())

# Revenue
from django.db.models import Sum
total = Booking.objects.filter(status='paid').aggregate(Sum('service__hourly_rate'))['service__hourly_rate__sum'] or 0
print(f"Total Revenue: ${total}")
print(f"Platform Commission (10%): ${float(total) * 0.10:.2f}")
```

---

## Emergency Procedures

### Database Crashed
```bash
# 1. Backup current database
copy db.sqlite3 db.sqlite3.backup.emergency

# 2. Try to recover from backup
copy db.sqlite3.backup db.sqlite3

# 3. If that fails, reset database
del db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Server Won't Start
```bash
# 1. Check for syntax errors
python manage.py check

# 2. Reinstall all packages
pip install -r requirements.txt --force-reinstall

# 3. Migrate database
python manage.py migrate

# 4. Try starting again
python manage.py runserver
```

### Users Can't Login
```bash
# 1. Reset a user's password
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.get(email='user@example.com')
user.set_password('temppassword123')
user.save()
# User can now login with temporary password and reset it

# 2. If database corrupted, restore from backup
copy db.sqlite3.backup db.sqlite3
```

### PDF/Invoice Generation Fails
```bash
# Check if xhtml2pdf is installed
pip install xhtml2pdf wkhtmltopdf

# On Windows, also install:
# Download wkhtmltopdf from: https://wkhtmltopdf.org/downloads.html
# Add to system PATH
```

### Email Not Sending
```python
# settings.py - Test with console backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Then check console when email action is triggered
# Once confirmed working, switch to SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Test manually
python manage.py shell
from django.core.mail import send_mail
send_mail('Test Subject', 'Test Body', 'from@example.com', ['to@example.com'])
```

---

## Security Checklist

### Application Security
- [ ] Change default SECRET_KEY
- [ ] Disable DEBUG in production
- [ ] HTTPS enabled
- [ ] CSRF protection enabled
- [ ] SQL injection prevention (using ORM)
- [ ] XSS protection enabled
- [ ] Authentication required for sensitive views
- [ ] Input validation on all forms
- [ ] File upload validation

### Data Security
- [ ] Regular backups scheduled
- [ ] Backup encryption configured
- [ ] Database password strong
- [ ] Email credentials in environment variables
- [ ] No sensitive data in logs
- [ ] Data access controls in place

### User Security
- [ ] Password hashing with Django's default
- [ ] Password minimum length requirement (6+ chars)
- [ ] Session timeout configured
- [ ] User account recovery option
- [ ] Privacy policy in place
- [ ] Terms of service in place

### Infrastructure Security
- [ ] Web server hardened
- [ ] Firewall configured
- [ ] Regular security updates applied
- [ ] DDoS protection
- [ ] SSL/TLS certificate valid
- [ ] .env file not in version control
- [ ] Secrets not in code

---

## Backup & Recovery Plan

### Backup Schedule
```
Daily: Automated backup at 2:00 AM
Weekly: Manual backup with verification
Monthly: Archive backup to secure storage
```

### Backup Commands
```bash
# Backup database
copy db.sqlite3 db.sqlite3.daily.%date:~-10%

# Backup media files
robocopy media media.backup /S /MIR

# Backup entire project
robocopy . backup_full /S /MIR /XD .venv

# Backup settings
copy babycare\babycare\settings.py settings.py.backup
```

### Recovery Procedures
```bash
# Restore from database backup
copy db.sqlite3.backup db.sqlite3

# Restore from media backup
robocopy media.backup media /S /MIR

# Restore from full backup
robocopy backup_full . /S /MIR
```

---

## Performance Monitoring

### Database Performance
```bash
# Check database file size
ls -lh db.sqlite3

# Monitor query count
# Add this to settings.py (development only)
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}
```

### Memory & CPU Usage
```bash
# Monitor processes
tasklist | findstr python

# Kill a process if needed
taskkill /PID process_id
```

### Server Responsiveness
```bash
# Check response time
time python manage.py shell

# Load test
# Use tools like: Apache Bench, Locust, or Jmeter
```

---

## Development vs Production Checklist

### Settings.py Changes for Production

```python
# ❌ DEVELOPMENT
DEBUG = True
ALLOWED_HOSTS = ['*']

# ✅ PRODUCTION
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

### Email Configuration

```python
# ❌ DEVELOPMENT (Console - no real emails)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ✅ PRODUCTION (SMTP - real emails)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

### Database

```python
# ❌ DEVELOPMENT
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ PRODUCTION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'babycareconnect',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': '5432',
    }
}
```

### Static Files

```python
# ❌ DEVELOPMENT
STATIC_URL = '/static/'

# ✅ PRODUCTION
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
```

### Security Settings (Production Only)

```python
# Add these to settings.py for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = {
    "default-src": ("'self'",),
}
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

---

## Regular Review Dates

Schedule these on your calendar:

| Task | Frequency | Next Date |
|------|-----------|-----------|
| Database backup | Daily | - |
| Error log review | Weekly | |
| Feature testing | Weekly | |
| User feedback review | Weekly | |
| Financial reconciliation | Monthly | |
| Security audit | Monthly | |
| Performance review | Quarterly | |
| Dependency updates | Quarterly | |
| Full system test | Quarterly | |

---

## Contact & Support

### Who to Contact
- **Database Issues:** Database Admin
- **Email/SMTP Issues:** IT Support
- **User Complaints:** Customer Service
- **Code Issues:** Development Team
- **Security Issues:** Security Officer

### Escalation Path
1. Try to fix yourself (follow Emergency Procedures)
2. Contact immediate supervisor
3. Contact development lead
4. Contact executive management

---

**Last Updated:** April 14, 2026
**Next Review:** May 14, 2026

For technical issues, refer to QUICK_REFERENCE.md
For detailed documentation, refer to PROJECT_GUIDE.md
