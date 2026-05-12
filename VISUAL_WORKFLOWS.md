# BabyCare Connect - Visual User Journey & Workflows

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                   BABYCARECONNECT PLATFORM               │
│                                                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │        FRONTEND (HTML/CSS/JavaScript)           │   │
│  │  - Service List, Booking, Dashboard, Chat       │   │
│  └───────────────┬─────────────────────────────────┘   │
│                  │                                       │
│  ┌───────────────▼─────────────────────────────────┐   │
│  │    DJANGO BACKEND (Python/Django)               │   │
│  │  - Views, Models, Business Logic, API           │   │
│  └───────────────┬─────────────────────────────────┘   │
│                  │                                       │
│  ┌───────────────▼─────────────────────────────────┐   │
│  │    DATABASE (SQLite)                            │   │
│  │  - Users, Services, Bookings, Messages          │   │
│  └─────────────────────────────────────────────────┘   │
│                                                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │    INTEGRATIONS                                 │   │
│  │  - Email Service (Gmail SMTP)                   │   │
│  │  - PDF Generator (xhtml2pdf)                    │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## Complete User Flows

### FLOW 1: Parent's Complete Journey

```
START
  │
  ├─→ [HOME PAGE]
  │    ├─ New user → "Register" button
  │    └─ Existing user → "Login" button
  │
  ├─→ [REGISTRATION]
  │    ├─ Name: "John Smith"
  │    ├─ Email: "john@example.com"
  │    ├─ Password: "SecurePass123"
  │    ├─ Role: Select "Parent (Looking for care)" ✓
  │    ├─ Terms: Agree ✓
  │    └─→ account created → Redirect to Login
  │
  ├─→ [LOGIN]
  │    ├─ Email: "john@example.com"
  │    ├─ Password: "SecurePass123"
  │    └─→ Authenticated → Redirect to Service List
  │
  ├─→ [SEARCH SERVICES]
  │    ├─ View all available services
  │    ├─ Search by location: "New York"
  │    ├─ Browse service cards
  │    └─→ Click "View Details" on service
  │
  ├─→ [SERVICE DETAILS PAGE]
  │    ├─ View: Title, description, hourly rate
  │    ├─ See provider info
  │    ├─ Check unavailable dates
  │    └─→ Click "Book Now"
  │
  ├─→ [BOOKING CONFIRMATION]
  │    ├─ Booking created with status: "PENDING"
  │    ├─ Email notification sent to parent
  │    └─→ Redirect to service detail page
  │
  ├─→ [WAIT FOR PROVIDER]
  │    │
  │    ├─ Provider confirms booking
  │    │  └─ Status changes: PENDING → CONFIRMED
  │    │  └─ Email: "Your booking was confirmed!"
  │    │
  │    └─ OR Provider rejects booking
  │       └─ Status: REJECTED
  │       └─ Email: "Your booking was declined"
  │
  ├─→ [MY BOOKINGS PAGE]
  │    ├─ View booking with status: "CONFIRMED"
  │    ├─ See booking details
  │    └─→ Wait for payment/completion
  │
  ├─→ [PAYMENT STAGE]
  │    ├─ Parent pays provider (external payment)
  │    ├─ Provider confirms payment
  │    └─ Status changes: CONFIRMED → PAID
  │
  ├─→ [DOWNLOAD INVOICE]
  │    ├─ Go to "My Bookings"
  │    ├─ Find "PAID" booking
  │    ├─ Click "Download Receipt" button
  │    ├─ PDF invoice downloads
  │    └─ Email receipt also sent
  │
  ├─→ [MESSAGING] (Optional - any time)
  │    ├─ Click "Messages"
  │    ├─ View conversation list
  │    ├─ Click provider name to chat
  │    ├─ Type & send messages
  │    └─ Real-time chat interface
  │
  ├─→ [SUPPORT]
  │    ├─ Go to "Contact"
  │    ├─ Fill form: name, email, subject, message
  │    ├─ Submit contact form
  │    └─ Receive confirmation email
  │
  └─→ [LOGOUT]
       └─→ Session ends

STATUS LEGEND:
🔵 PENDING   = Waiting for provider confirmation
🟢 CONFIRMED = Provider approved, awaiting payment
💰 PAID      = Payment received, invoice available
❌ REJECTED  = Provider declined booking
```

---

### FLOW 2: Provider's Complete Journey

```
START
  │
  ├─→ [HOME PAGE]
  │    └─ Register or Login
  │
  ├─→ [REGISTRATION]
  │    ├─ Name: "Jane Smith"
  │    ├─ Email: "jane.provider@example.com"
  │    ├─ Password: "SecurePass456"
  │    ├─ Role: Select "Provider (Offering care)" ✓
  │    └─→ Account created
  │
  ├─→ [LOGIN]
  │    ├─ Email: "jane.provider@example.com"
  │    ├─ Password: "SecurePass456"
  │    └─→ Redirected to Provider Dashboard
  │
  ├─→ [PROVIDER DASHBOARD]
  │    ├─ Overview: Services, Bookings, Earnings
  │    ├─ See total earnings (from PAID bookings)
  │    ├─ Monthly earnings report
  │    └─→ Navigation to add service or manage
  │
  ├─→ [ADD SERVICE]
  │    ├─ Fill service details:
  │    │   ├─ Title: "Daytime Nanny Service"
  │    │   ├─ Description: "Professional childcare..."
  │    │   ├─ Hourly Rate: "25.00"
  │    │   ├─ Location: "New York, NY"
  │    │   └─ Photo: Upload image (optional)
  │    ├─ Click "Create Listing"
  │    ├─ Service created with is_available=True
  │    └─→ Service visible to all parents
  │
  ├─→ [MANAGE AVAILABILITY]
  │    ├─ For each service:
  │    │   ├─ Click "Manage Availability"
  │    │   ├─ Select dates you're NOT available
  │    │   ├─ Example: Block "2026-05-15"
  │    │   └─ Click "Block Date"
  │    └─ Parents see these as unavailable
  │
  ├─→ [INCOMING BOOKINGS]
  │    │
  │    ├─ New booking arrives from parent
  │    ├─ Email notification: "You have a new booking!"
  │    │
  │    └─→ Go to Dashboard → View Bookings
  │
  ├─→ [CONFIRM/REJECT BOOKING]
  │    │
  │    ├─ For each PENDING booking:
  │    │   ├─ Option 1: Click "✓ Confirm" 
  │    │   │   └─ Status: PENDING → CONFIRMED
  │    │   │   └─ Parent notified via email
  │    │   │
  │    │   └─ Option 2: Click "✗ Reject"
  │    │       └─ Status: REJECTED
  │    │       └─ Parent can rebook
  │    │
  │    └─→ Wait for parent to pay
  │
  ├─→ [RECEIVE PAYMENT]
  │    ├─ Parent pays (external method)
  │    ├─ Parent notifies you of payment
  │    │
  │    └─→ Go to Dashboard
  │        └─ Find CONFIRMED booking
  │        └─ Click "💰 Confirm Payment"
  │
  ├─→ [PAYMENT CONFIRMATION]
  │    ├─ Status: CONFIRMED → PAID
  │    ├─ You earn: Service Rate × 90%
  │    │   Example: $25 × 90% = $22.50
  │    ├─ Platform takes: Service Rate × 10%
  │    │   Example: $25 × 10% = $2.50
  │    ├─ Invoice PDF automatically generated
  │    ├─ Invoice emailed to parent
  │    └─ Earnings updated in Dashboard
  │
  ├─→ [VIEW EARNINGS]
  │    ├─ Dashboard shows:
  │    │   ├─ "Total Earnings": Sum of all paid bookings
  │    │   ├─ "Monthly Report": Breakdown by month
  │    │   └─ "Net Pay": Amount after 10% commission
  │    │
  │    └─ Example:
  │        ├─ Service Rate: $25/hour
  │        ├─ Commission: 10% = $2.50
  │        └─ Your Earnings: 90% = $22.50
  │
  ├─→ [MESSAGING] (Optional - any time)
  │    ├─ Go to "Messages"
  │    ├─ See all parent conversations
  │    ├─ Click to chat with parents
  │    └─ Real-time messaging interface
  │
  ├─→ [CONTACT] (Optional)
  │    ├─ Submit contact form if have questions
  │    └─ Support team will respond
  │
  └─→ [LOGOUT]
       └─→ Session ends

NET EARNING CALCULATION:
Parent pays:                            $100
Platform commission (10%):               $10
Provider receives (90%):                 $90
                                    ─────────
Total: Provider gets paid                $90
```

---

### FLOW 3: Admin's Journey

```
START
  │
  ├─→ [ADMIN DASHBOARD]
  │    ├─ Only accessible by admin users
  │    ├─ URL: /admin_dashboard/
  │    │
  │    └─→ Overview Section
  │        ├─ User Statistics:
  │        │  ├─ Total Parents: 42
  │        │  ├─ Total Providers: 15
  │        │  └─ Total Admins: 2
  │        │
  │        ├─ Booking Statistics:
  │        │  ├─ Total Bookings: 127
  │        │  ├─ Pending: 8
  │        │  ├─ Confirmed: 31
  │        │  └─ Paid: 88
  │        │
  │        ├─ Financial Statistics:
  │        │  ├─ Total Revenue: $2,200 (all paid bookings)
  │        │  ├─ Platform Commission (10%): $220
  │        │  ├─ Provider Payouts (90%): $1,980
  │        │  └─ Net Profit: $220
  │        │
  │        └─ Top Services:
  │           ├─ 1. Daytime Nanny (15 bookings)
  │           ├─ 2. Babysitting (12 bookings)
  │           └─ 3. Tutoring (10 bookings)
  │
  ├─→ [DJANGO ADMIN PANEL]
  │    ├─ URL: /admin/
  │    ├─ Superuser only
  │    │
  │    └─→ Manage:
  │        ├─ Users (Create, Edit, Delete)
  │        ├─ Services (View, Edit, Delete)
  │        ├─ Bookings (View, Modify Status)
  │        ├─ Messages (View, Delete)
  │        └─ Contacts (View, Archive)
  │
  ├─→ [MONITORING & MAINTENANCE]
  │    │
  │    ├─ Daily:
  │    │   ├─ Check new registrations
  │    │   ├─ Review error logs
  │    │   └─ Verify server is running
  │    │
  │    ├─ Weekly:
  │    │   ├─ Generate activity report
  │    │   ├─ Review user feedback
  │    │   ├─ Backup database
  │    │   └─ Monitor database size
  │    │
  │    └─ Monthly:
  │        ├─ Generate financial report
  │        ├─ Calculate total earnings
  │        ├─ Review system performance
  │        └─ Plan improvements
  │
  ├─→ [USER MANAGEMENT]
  │    ├─ Create new admin users
  │    ├─ Modify user roles (parent→provider)
  │    ├─ Suspend inactive accounts
  │    ├─ Reset user passwords
  │    └─ Delete inappropriate accounts
  │
  ├─→ [SERVICE MANAGEMENT]
  │    ├─ Review new services
  │    ├─ Remove inappropriate services
  │    ├─ Verify service details
  │    └─ Monitor service quality
  │
  ├─→ [BOOKING MANAGEMENT]
  │    ├─ View all bookings
  │    ├─ Modify booking status if needed
  │    ├─ Handle disputes
  │    └─ Process refunds (if applicable)
  │
  ├─→ [FINANCIAL MANAGEMENT]
  │    ├─ Track platform revenue
  │    ├─ Monitor payment processing
  │    ├─ Generate financial reports
  │    ├─ Calculate provider payouts
  │    └─ Plan budget
  │
  ├─→ [DATABASE BACKUP]
  │    ├─ Schedule automatic backups
  │    ├─ Test backup recovery
  │    ├─ Archive old backups
  │    └─ Monitor backup storage
  │
  ├─→ [SECURITY MANAGEMENT]
  │    ├─ Monitor suspicious activity
  │    ├─ Review access logs
  │    ├─ Update security policies
  │    └─ Enforce password policies
  │
  └─→ [LOGOUT]
       └─→ Session ends
```

---

## Feature Interaction Map

```
                    ┌─────────────────────────────────────┐
                    │    AUTHENTICATION                    │
                    │  Register / Login / Logout           │
                    └──────────────┬──────────────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
          ▼                        ▼                        ▼
    ┌──────────────┐        ┌──────────────┐        ┌──────────────┐
    │    PARENT    │        │   PROVIDER   │        │    ADMIN     │
    └──────────────┘        └──────────────┘        └──────────────┘
          │                        │                        │
          ├─ Search Services       ├─ Add Service           ├─ Dashboard
          ├─ View Details          ├─ Manage Dates          ├─ Django Admin
          ├─ Book Service          ├─ Accept Bookings       ├─ Monitor Stats
          ├─ My Bookings           ├─ Confirm Payment       ├─ Manage Users
          ├─ Download Invoice      ├─ Send Invoice          ├─ View Reports
          ├─ Chat                  ├─ View Earnings         ├─ Backup DB
          ├─ Messages              ├─ Chat                  └─ Security Audit
          └─ Contact               ├─ Messages
                                   └─ Contact
                                   
    ┌─────────────────────────────────────────────────────────┐
    │              SHARED FEATURES                            │
    │  Login │ Logout │ Contact │ Chat/Messages │ Homepage    │
    └─────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    PARENT                                    │
│                                                               │
│  1. Searches for service                                    │
│  2. Views service details                                   │
│  3. Clicks "Book Now"                                       │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ POST /create_booking/<service_id>
                       ▼
        ┌──────────────────────────────────┐
        │   CREATE BOOKING                 │
        │  - parent: John (User)           │
        │  - service: Nanny (Service)      │
        │  - start_date: 2026-04-15        │
        │  - status: pending               │
        └──────────────┬───────────────────┘
                       │
                       │ Save to Database
                       ▼
        ┌──────────────────────────────────┐
        │      DATABASE                    │
        │                                  │
        │  ✓ Booking record created        │
        │  ✓ Status: PENDING               │
        │  ✓ Email notification sent       │
        │  ✓ Parent redirected             │
        └──────────────┬───────────────────┘
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
    ┌──────────────────┐    ┌──────────────────┐
    │  EMAIL TO PARENT │    │  EMAIL TO        │
    │                  │    │  PROVIDER        │
    │ "New booking!"   │    │ "You have a new  │
    │                  │    │  booking!"       │
    └──────────────────┘    └────────┬─────────┘
                                     │
                                     ▼
                          ┌─────────────────────────────┐
                          │       PROVIDER              │
                          │                             │
                          │  1. Reviews booking         │
                          │  2. Logs to dashboard       │
                          │  3. Clicks "Confirm"        │
                          └────────────┬────────────────┘
                                       │
                                       │ Update booking status
                                       ▼
                          ┌─────────────────────────────┐
                          │  Status: PENDING → CONFIRMED│
                          │  Email parent confirmation  │
                          │  Provider awaits payment    │
                          └─────────────────────────────┘
```

---

## Technology Stack Visual

```
┌──────────────────────────────────────────────────────────┐
│                   WEB BROWSER                             │
│  (Chrome, Firefox, Safari, Edge)                          │
└────────────────────────┬─────────────────────────────────┘
                         │
                         │ HTTP/HTTPS
                         ▼
    ┌────────────────────────────────────┐
    │     DJANGO WEB SERVER (Port 8000)  │
    │                                    │
    │  ┌────────────────────────────┐   │
    │  │  FRONTEND (HTML/CSS/JS)    │   │
    │  │  - Templates               │   │
    │  │  - Bootstrap 5.3.2         │   │
    │  │  - JavaScript Forms        │   │
    │  └────────────────────────────┘   │
    │                                    │
    │  ┌────────────────────────────┐   │
    │  │  DJANGO BACKEND (Python)   │   │
    │  │  - Views (15+ views)       │   │
    │  │  - URL Routing             │   │
    │  │  - Form Handling           │   │
    │  │  - Authentication          │   │
    │  │  - Email System            │   │
    │  │  - PDF Generation          │   │
    │  └────────────────────────────┘   │
    └────────────────┬───────────────────┘
                     │
    ┌────────────────┴───────────────────┐
    │                                    │
    ▼                                    ▼
┌──────────────────┐              ┌──────────────────┐
│   DATABASE       │              │  EMAIL SERVICE   │
│  (SQLite3)       │              │  (Gmail SMTP)    │
│                  │              │                  │
│ ├─ Users         │              │ Sends:           │
│ ├─ Services      │              │ - Welcome email  │
│ ├─ Bookings      │              │ - Confirmations  │
│ ├─ Messages      │              │ - Invoices       │
│ ├─ Availability  │              │ - Support reply  │
│ └─ Contacts      │              │                  │
└──────────────────┘              └──────────────────┘
```

---

## Booking Status Lifecycle

```
START
  │
  ├─→ Parent submits booking
  │
  ├─→ PENDING ⭕
  │    ├─ Email: Parent booking created
  │    ├─ Email: Provider has new booking
  │    ├─ Party: Waiting for confirmation
  │    │
  │    └─→ Provider action:
  │        ├─ Confirm? → CONFIRMED
  │        └─ Reject? → REJECTED ❌
  │
  ├─→ CONFIRMED ✓
  │    ├─ Email: Parent booking approved
  │    ├─ Email: Provider awaiting payment
  │    ├─ Parent: Makes payment (external)
  │    │
  │    └─→ Provider action:
  │        └─ Confirm payment? → PAID
  │
  ├─→ PAID 💰
  │    ├─ Email: Invoice sent to parent
  │    ├─ Parent: Can download receipt
  │    ├─ Provider: Earns 90% of rate
  │    ├─ Platform: Gets 10% commission
  │    │
  │    └─→ Booking completed ✓
  │
  ├─→ REJECTED ❌
  │    ├─ Email: Parent booking declined
  │    ├─ Parent: Can book other services
  │    └─→ Booking ends
  │
  └─→ END
```

---

## Commission Flow

```
PARENT PAYS $100 for Babysitting
         │
         │
         ├──→ 10% ($10) to PLATFORM
         │     └─ Covers server, email, support
         │
         └──→ 90% ($90) to PROVIDER
              └─ Paid when clicking confirm payment
              

EXAMPLE TRANSACTION:

Service: "Daytime Nanny"
Rate: $25/hour

Booking created
  ↓
Status: PAID (confirmed by provider)
  ↓
Calculation:
  - Amount: $25
  - Commission (10%): $2.50
  - Payout (90%): $22.50
  ↓
Provider receives: $22.50
Platform keeps: $2.50
```

---

## Monthly Earnings Report Example

```
PROVIDER DASHBOARD - MONTHLY REPORT

Provider: Jane Smith
Report Period: April 2026

┌────────────────────────────────┐
│  SERVICE: Daytime Nanny        │
├────────────────────────────────┤
│  April 1  │ $25 │ PAID    ✓    │
│  April 3  │ $25 │ PAID    ✓    │
│  April 7  │ $25 │ PAID    ✓    │
│  April 10 │ $25 │ PAID    ✓    │
│  April 15 │ $25 │ CONFIRMED   │
└────────────────────────────────┘

EARNINGS SUMMARY:
  Total Bookings: 5
  Confirmed: 1 (awaiting payment)
  Paid: 4
  
FINANCIAL BREAKDOWN:
  Total Service Value: $125.00
  Platform Commission (10%): $12.50
  Your Earnings (90%): $112.50
  
MONTHLY STATUS:
  ✓ 4 payments received = $112.50
  ⏳ 1 pending = $22.50 (once paid)
```

---

## Dashboard Widgets Summary

### Parent Dashboard
```
┌─────────────────────────────┐
│ MY BOOKINGS                 │
├─────────────────────────────┤
│ Pending:    2               │
│ Confirmed:  1               │
│ Paid:       5               │
│ Total:      8               │
└─────────────────────────────┘

┌─────────────────────────────┐
│ QUICK ACTIONS               │
├─────────────────────────────┤
│ ▶ Search Services           │
│ ▶ My Bookings               │
│ ▶ Messages                  │
│ ▶ Download Invoice          │
└─────────────────────────────┘
```

### Provider Dashboard
```
┌─────────────────────────────┐
│ SERVICES                    │
├─────────────────────────────┤
│ Active:     5               │
│ Available:  26 dates        │
│ Bookings:   12              │
└─────────────────────────────┘

┌─────────────────────────────┐
│ EARNINGS THIS MONTH         │
├─────────────────────────────┤
│ Paid:       $450.00 (90%)   │
│ Pending:    $250.00 (90%)   │
│ Total:      $700.00         │
└─────────────────────────────┘
```

### Admin Dashboard
```
┌─────────────────────────────┐
│ PLATFORM METRICS            │
├─────────────────────────────┤
│ Total Users:    57          │
│ Total Bookings: 127         │
│ Revenue (10%):  $220.00     │
│ Payouts (90%):  $1,980.00   │
└─────────────────────────────┘
```

---

**This visual guide shows the complete system flow. Refer to PROJECT_GUIDE.md for detailed instructions.**
