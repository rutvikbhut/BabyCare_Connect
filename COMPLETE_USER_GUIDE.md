# BabyCare Connect - Complete User Guide
**All Features & Step-by-Step Instructions**

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [User Registration](#user-registration)
3. [User Login](#user-login)
4. [Parent Features](#parent-features)
5. [Provider Features](#provider-features)
6. [Admin Features](#admin-features)
7. [Troubleshooting](#troubleshooting)

---

## Getting Started

### System Requirements
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection
- Valid email address

### Access the Application
1. Open your web browser
2. Navigate to: `http://127.0.0.1:8000/` (Local development)
3. You should see the **BabyCare Connect** homepage

### Navigation Menu
Once logged in, the top navigation bar shows:
- **Home** - Go to homepage
- **Services** - Browse all childcare services
- **Profile Dropdown** - Your account options (shows your name)
- **Logout** - Sign out of your account

---

## User Registration

### Step 1: Access Registration Page
1. Click **Register** link in the top-right corner (when not logged in)
2. Or navigate to: `http://127.0.0.1:8000/register/`

### Step 2: Choose Your Role
You must select ONE role:
- **Parent** - Looking for childcare services
- **Provider** - Offering childcare services

### Step 3: Fill Registration Form
Complete all fields:

| Field | Details |
|-------|---------|
| **First Name** | Your first name (required) |
| **Last Name** | Your last name (required) |
| **Email** | Your email address (used for login, must be unique) |
| **Phone** | Your contact phone number (required) |
| **Address** | Your full address (required) |
| **Password** | At least 8 characters, mix of letters & numbers (required) |
| **Confirm Password** | Re-enter password exactly (must match) |

### Step 4: Submit Registration
1. Click **"Register"** button
2. **Success Message**: "✓ Registration successful! Please login."
3. You are redirected to login page

### Registration Rules
- ❌ Email already exists → Error: "Email already registered"
- ❌ Passwords don't match → Error: "Passwords do not match"
- ❌ Invalid phone format → Error: "Invalid phone number"
- ❌ Password too short → Error: "Password must be at least 8 characters"

---

## User Login

### Step 1: Access Login Page
1. Click **Login** link in top-right corner
2. Or navigate to: `http://127.0.0.1:8000/login/`

### Step 2: Enter Login Credentials
Fill in the login form:
- **Email**: The email you registered with
- **Password**: Your password

### Step 3: Click Login
1. Click **"Login"** button
2. **Success**: You see dashboard with your name in top-right

### Login Error Messages
| Error | Solution |
|-------|----------|
| Invalid email or password | Check email and password spelling |
| Email not registered | Go to Register page first |
| Account inactive | Contact admin for account activation |

### Forgot Password
1. Click **"Forgot Password?"** link on login page
2. Enter your email address
3. Click **"Reset Password"**
4. Check your email for reset link
5. Follow the link and create new password

---

## Parent Features

### 1. Browse Services

#### Step 1: Go to Services Page
1. Click **"Services"** in top navigation menu
2. Or click **"Browse Services"** on homepage

#### Step 2: Search Services
**Search by Location:**
- Enter location in search box (e.g., "New York" or "Brooklyn, NY")
- Click **"Search"** button
- See filtered results

**View All Services:**
- Leave search box empty
- Click **"Search"** or page loads all services

#### Step 3: View Service Cards
Each service card shows:
- 📷 Service image (or placeholder)
- 📌 **Service Title** (e.g., "Daytime Nanny")
- 💰 **Hourly Rate** (e.g., "$25/hour")
- 📍 **Location** (e.g., "Brooklyn, NY")
- 👤 **Provider Name**
- 🌐 **Online Status** (green dot = online now)

#### Step 4: Click Service Card
1. Click on any service to view **details**
2. Goes to **Service Detail Page**

---

### 2. View Service Details

#### Detail Page Information
Shows:
- 📷 Large service image
- 📌 **Service Title**
- 💰 **Hourly Rate**
- 📍 **Location**
- 📝 **Full Description** (what the service includes)

#### Provider Information
Shows:
- 👤 **Provider Name**
- ⏰ **Member Since** (month/year they joined)
- 🌐 **Online Status** (green checkmark if online)

#### Availability Calendar
Shows **Already Booked / Unavailable Dates**:
- 🟥 Red section = dates the provider is unavailable
- 🟩 Green message = "Provider is free for all dates!" (if available)

#### Book Service
1. Scroll to bottom of page
2. Click **"📚 Book Now"** button (green)
3. See message: "Click to request this service from the provider"

---

### 3. Book a Service

#### Step 1: Review Service Details
1. Read service description carefully
2. Check provider information
3. Verify availability

#### Step 2: Click Book Now
1. Click **"📚 Book Now"** button
2. Must be LOGGED IN (required)

#### Step 3: Booking Confirmation
**Success Message**: "✓ Booking request for '[Service Name]' sent successfully!"

**Booking Created with Status**: **PENDING**
- You can now see it in "My Bookings"
- Provider gets notification
- Provider can confirm or reject

#### Step 4: Wait for Confirmation
- Check "**My Bookings**" in profile menu
- Status shows: 🟡 **PENDING** (yellow badge)
- Provider will confirm within 24 hours typically

#### Booking Status Flow
```
PENDING (you booked)
    ↓
CONFIRMED (provider approved)
    ↓
PAID (confirmed payment)
    ↓
COMPLETED
```

### Duplicate Booking Prevention
- You cannot have 2 PENDING or CONFIRMED bookings for same service
- Message: "You already have a pending booking for this service."
- Must wait for first booking to complete or cancel it

---

### 4. View My Bookings

#### Step 1: Access My Bookings
1. Click profile dropdown (top-right with your name)
2. Click **"My Bookings"**
3. Or navigate to: `http://127.0.0.1:8000/parent-bookings/`

#### Step 2: View Your Bookings Table
Shows all bookings you made:

| Column | Information |
|--------|-------------|
| **Service Name** | What service you booked |
| **Provider** | Who is providing the service |
| **Status** | 🟡 Pending / 🟢 Confirmed / ⚫ Paid |
| **Booked Date** | When you made the booking |
| **Total Price** | Cost of service |
| **Actions** | Download invoice (if paid) |

#### Step 3: Check Status
- 🟡 **PENDING** = Waiting for provider confirmation (1-2 days)
- 🟢 **CONFIRMED** = Provider approved, service booked
- ⚫ **PAID** = Payment received, booking complete
- ❌ **CANCELLED** = Provider rejected the booking

#### Step 4: Download Invoice (If Paid)
1. Find booking with status **"PAID"**
2. Click **"📄 Download Invoice"** button
3. PDF invoice downloads to your computer
4. Shows: service details, price, dates, provider info

---

### 5. Messaging & Chat

#### Step 1: Access Inbox
1. Click profile dropdown (top-right)
2. Click **"Inbox"** or **"Messages"**
3. Or navigate to: `http://127.0.0.1:8000/inbox/`

#### Step 2: View Conversations
Shows list of all providers you've chatted with:
- 👤 **Provider Name**
- 💬 **Last Message** (preview)
- 🔴 **Unread Count** (if new messages)
- 🏷️ **Role Badge** (shows "Provider")

#### Step 3: Open Chat
1. Click on provider name in conversation list
2. Opens **Chat Room** window
3. Shows full conversation history

#### Step 4: Send Message
1. Type your message in text box at bottom
2. Click **"Send Message"** button
3. Message appears immediately
4. Provider gets notification

#### Chat Features
- 💬 See all previous messages
- ✅ Message timestamps
- 👥 See who sent each message
- 🟢 Shows if provider is typing
- ⏱️ Last activity timestamp

#### When Conversations Start
Messages appear ONLY after:
1. You book a service (PENDING booking created) → Auto-creates conversation with provider
2. Provider confirms your booking (CONFIRMED status)
3. You initiate massage requesting something

---

## Provider Features

### 1. Add a Service

#### Step 1: Access Add Service Page
1. Click profile dropdown (top-right)
2. Click **"Add Service"**
3. Or navigate to: `http://127.0.0.1:8000/add-service/`

#### Step 2: Fill Service Information

| Field | Required | Details |
|-------|----------|---------|
| **Service Title** | ✅ | Name of service (e.g., "Daytime Nanny") |
| **Description** | ✅ | What the service includes (200+ characters recommended) |
| **Location** | ✅ | Where service is provided (e.g., "Brooklyn, NY") |
| **Hourly Rate** | ✅ | Price per hour (number only, e.g., 25) |
| **Service Image** | ❌ | Optional - upload image (JPG/PNG) |

#### Step 3: Complete Form Examples

**Example 1 - Nanny Service:**
- Title: "Daytime Nanny Services"
- Description: "Professional nanny for children 2-12 years old. Services include meal prep, homework help, supervised playtime, and educational activities. Background checked and certified in first aid."
- Location: "Manhattan, NY"
- Rate: "28"
- Image: (optional photo of workspace)

**Example 2 - Tutoring Service:**
- Title: "Math & Science Tutoring"
- Description: "Expert tutoring in mathematics and sciences for grades 6-12. Specialized in algebra, geometry, biology, and chemistry. Interactive learning with real examples. Progress reports provided."
- Location: "Brooklyn, NY"
- Rate: "35"

#### Step 4: Upload Image (Optional)
1. Click **"Choose File"** button
2. Select image from computer
3. JPG, PNG, or GIF formats accepted
4. Image displays on service detail page

#### Step 5: Submit Service
1. Click **"Add Service"** button
2. **Success Message**: "✓ Service '[Title]' created successfully!"
3. You're redirected to your dashboard

#### Service Validation
- ❌ Missing required field → Error: "[Field] is required"
- ❌ Rate is not a number → Error: "Rate must be a number"
- ❌ Rate is negative → Error: "Rate must be positive"
- ❌ Image too large → Error: "Image must be less than 5MB"

---

### 2. Manage Service Availability

#### Step 1: Access Manage Availability
1. Go to **Provider Dashboard** (from profile menu)
2. Find your service in the services list
3. Click **"📅 Manage Availability"** button
4. Or navigate to: `http://127.0.0.1:8000/manage-availability/<service_id>/`

#### Step 2: View Calendar
Shows a calendar with:
- ✅ **Green dates** = Available for bookings
- ❌ **Red dates** = Blocked (unavailable)

#### Step 3: Block Dates
1. Click on any date (single day)
2. Date turns RED (blocked)
3. Click **"Save"** button
4. Message: "✓ Availability updated!"

#### Step 4: Unblock Dates
1. Click on RED date
2. Date turns GREEN (available)
3. Click **"Save"** button
4. Message: "✓ Availability updated!"

#### Step 5: Block Multiple Days
1. Use "Blocked Dates" section
2. Enter start date and end date
3. Click **"Block Period"** button
4. All dates in range turn RED

#### Availability Purpose
- Parents cannot book you on blocked dates
- Parents see "Unavailable" on service detail page
- Use for: vacations, sick days, maintenance, other commitments

---

### 3. Provider Dashboard

#### Step 1: Access Dashboard
1. Click profile dropdown (top-right)
2. Click **"Provider Dashboard"**
3. Or navigate to: `http://127.0.0.1:8000/provider-dashboard/`

#### Step 2: View Dashboard Statistics
Shows your key metrics:

| Metric | Meaning |
|--------|---------|
| **Total Bookings** | All bookings (any status) |
| **Pending Requests** | Waiting for your confirmation |
| **Confirmed Bookings** | You approved, awaiting payment |
| **Earnings** | Income from paid bookings |
| **Monthly Report** | Earnings breakdown by month |

#### Step 3: View Bookings Table
Shows all bookings for your services:

| Column | Shows |
|--------|-------|
| **Parent** | Who booked |
| **Service** | What they booked |
| **Status** | 🟡 Pending / 🟢 Confirmed / ⚫ Paid |
| **Actions** | Confirm/Reject/Mark Paid buttons |
| **Rate** | Hourly rate |
| **Earning** | How much you'll earn |

#### Step 4: Manage Bookings
See next section "Confirm/Reject Bookings"

---

### 4. Confirm or Reject Bookings

#### Booking Status States

**PENDING** (Yellow Badge)
- Parent just booked
- Waiting for your decision
- Action buttons: ✅ **Confirm** or ❌ **Reject**

**CONFIRMED** (Green Badge)
- You approved the booking
- Parent can see service is theirs
- Action button: 💰 **Confirm Payment**

**PAID** (Gray Badge)
- Payment confirmed
- Booking complete
- Service: No actions available

**CANCELLED** (Gray Badge)
- You rejected the booking
- No actions available

#### Step 1: Review Pending Booking
1. Go to **Provider Dashboard**
2. Look for 🟡 **PENDING** status bookings
3. Click parent name to see their profile
4. Review their information

#### Step 2: Confirm Booking
**If you accept the booking:**
1. Click **"✅ Confirm"** button
2. **Success Message**: "Booking updated to confirmed."
3. Status changes from 🟡 **PENDING** → 🟢 **CONFIRMED**
4. Parent gets notified immediately
5. Conversation/chat opens automatically

#### Step 3: Reject Booking
**If you cannot provide service:**
1. Click **"❌ Reject"** button
2. **Success Message**: "Booking updated to cancelled."
3. Status changes to ❌ **CANCELLED**
4. Parent is notified
5. Parent can book another provider's service

#### Step 4: Confirm Payment
**When service is provided and paid:**
1. Look for 🟢 **CONFIRMED** status bookings
2. Click **"💰 Confirm Payment"** button
3. **Success Message**: "Booking marked as paid."
4. Status changes → ⚫ **PAID**
5. Earning added to your total

---

### 5. Track Earnings

#### View Monthly Report
1. Go to **Provider Dashboard**
2. Scroll to **"Monthly Report"** section
3. Shows earnings breakdown:
   - January: $450
   - February: $320
   - March: $580
   - etc.

#### View Total Earnings
1. **Provider Dashboard** shows big number: "💰 $1,350"
2. This is total from ALL paid bookings
3. From confirmed payments = from 🟢 CONFIRMED → ⚫ PAID bookings

#### Track Individual Booking Earnings
1. Go to bookings table
2. Column "Earning" shows: $25, $35, $28, etc.
3. Only counts when status = PAID

#### Payment Calculation
```
Earning = Hourly Rate × Service Hours
Example: $30/hour rate = $30 earning per hour
```

---

### 6. Messaging with Parents

#### Conversation Starts When
1. Parent books your service (creates auto-conversation)
2. You confirm the booking (both can chat)
3. You receive message from parent

#### Access Messages
1. Click profile dropdown
2. Click **"Inbox"** or **"Messages"**
3. See list of parents who booked from you

#### View Conversation
1. Click parent name
2. Opens chat window
3. Shows all messages with that parent

#### Send Message
1. Type message in text box
2. Click **"Send"** button
3. Message sends immediately
4. Parent sees it in their inbox

#### Message Features
- 📝 Full message history
- ✅ Timestamps on each message
- 👤 Shows who sent each message
- 'Typing' indicator when parent is typing
- Last activity shown

---

## Admin Features

### Access Admin Panel
1. Login with **admin account**
2. Navigate to: `http://127.0.0.1:8000/admin/`
3. Enter admin email and password

### Admin Dashboard
Shows statistics:
- Total users registered
- Total services listed
- Total bookings made
- Total revenue from paid bookings

---

### Manage Users

#### Step 1: Go to User Management
1. Click **"Users"** in admin panel
2. See list of all registered users

#### Step 2: View User Information
| Field | Shows |
|-------|-------|
| **Email** | Login email |
| **First Name** | User's first name |
| **Role** | Parent or Provider |
| **Active** | ✅ Yes or ❌ No |
| **Joined Date** | Registration date |

#### Step 3: Edit User
1. Click on user email
2. Edit any field
3. Click **"Save"**

#### Step 4: Deactivate User
1. Uncheck **"Active"** checkbox
2. Click **"Save"**
3. User cannot login anymore

#### Step 5: Delete User
1. Click user email
2. Scroll to bottom
3. Click **"Delete"** button
4. ⚠️ Cannot be undone

---

### Manage Services

#### Step 1: Go to Services
1. Click **"Services"** in admin panel
2. See all services from all providers

#### Step 2: View Service Info
| Field | Shows |
|-------|-------|
| **Title** | Service name |
| **Provider** | Who offers it |
| **Location** | Where offered |
| **Hourly Rate** | Price per hour |
| **Created** | When added |

#### Step 3: Edit Service
1. Click service title
2. Edit title, description, rate, image
3. Click **"Save"**

#### Step 4: Delete Service
1. Click service title
2. Click **"Delete"** button
3. Service removed from platform

---

### Manage Bookings

#### Step 1: Go to Bookings
1. Click **"Bookings"** in admin panel
2. See all bookings on platform

#### Step 2: View Booking Info
| Field | Shows |
|-------|-------|
| **Parent** | Who booked |
| **Service** | What they booked |
| **Status** | Current status |
| **Booking Date** | When they booked |
| **Start Date** | When service begins |

#### Step 3: Change Booking Status
1. Click booking ID
2. Change "Status" dropdown
3. Options: PENDING, CONFIRMED, PAID, CANCELLED
4. Click **"Save"**

#### Step 4: View Payment Info
1. Click booking
2. See "Net Pay" (provider's earnings)
3. Calculate: hourly_rate × hours

---

### View Login History

#### Step 1: Go to Login History
1. Click **"Login History"** in admin panel
2. See all login/logout events

#### Step 2: View History Details
| Field | Shows |
|-------|-------|
| **User Email** | Who logged in |
| **Login Time** | When they logged in |
| **Logout Time** | When they logged out |
| **Active** | Still logged in? |
| **IP Address** | Computer IP (if tracked) |

#### Step 3: Filter by User
1. Click **"Filter by User"** on right
2. Select specific user
3. See only their login history

#### Step 4: Search by Date
1. Use date filter
2. See logins/logouts on specific date

---

### View Messages

#### Step 1: Go to Messages
1. Click **"Messages"** in admin panel
2. See all chat messages

#### Step 2: Filter by Conversation
1. Select user from dropdown
2. See all messages from one pair
3. Or see all platform messages

#### Step 3: Monitor Communication
- Ensure appropriate conversation
- Check for spam/abuse
- Delete inappropriate messages if needed

---

### View Availability

#### Step 1: Go to Availability
1. Click **"Availability"** in admin panel
2. See all blocked dates

#### Step 2: Check Provider Schedules
| Field | Shows |
|-------|-------|
| **Service** | Which service |
| **Provider** | Who blocked it |
| **Unavailable Date** | Date blocked |

#### Step 3: Manage Blocks
1. Click unavailable date entry
2. Edit or delete
3. Allows changing provider schedules if needed

---

## Troubleshooting

### Login Issues

**Problem**: "Invalid email or password"
- ✅ Check email spelling exactly
- ✅ Check password spelling exactly
- ✅ Make sure Caps Lock is OFF
- ✅ If email not registered, go to Register page

**Problem**: "Email not registered"
- ✅ You haven't registered yet
- ✅ Go to Register page
- ✅ Use different email if already registered as another user

**Problem**: "Cannot login as provider/parent"
- ✅ Check your registered role (check admin panel)
- ✅ Role is set during registration and cannot be changed
- ✅ Create new account with correct role

---

### Booking Issues

**Problem**: "Only parents can book services"
- ✅ You are logged in as a Provider
- ✅ Providers cannot book services
- ✅ Use a Parent account to book

**Problem**: "You already have a pending booking for this service"
- ✅ You already booked this service
- ✅ Wait for provider confirmation
- ✅ Contact provider via chat if issue

**Problem**: "Cannot see booking after booking"
- ✅ Check "My Bookings" page (takes 2-3 seconds to appear)
- ✅ Refresh page
- ✅ Check if you're logged in correctly

---

### Message/Chat Issues

**Problem**: "No messages/conversations showing"
- ✅ Conversations only appear after:
  - You book a service (PENDING booking created)
  - Provider confirms your booking
- ✅ You haven't booked any services yet
- ✅ Book a service first, then messages appear

**Problem**: "Cannot send message"
- ✅ Are you logged in?
- ✅ Do you have a confirmed booking?
- ✅ Check internet connection
- ✅ Refresh the page

---

### Service/Provider Issues

**Problem**: "Cannot add service as parent"
- ✅ Only Providers can add services
- ✅ You registered as a Parent
- ✅ Create new Provider account
- ✅ Roles cannot be changed

**Problem**: "Service not showing search results"
- ✅ Check service location matches search
- ✅ Service might be newly added (takes few seconds)
- ✅ Refresh the page
- ✅ Clear browser cache

**Problem**: "Cannot confirm bookings"
- ✅ Only the service provider can confirm
- ✅ Service must be YOUR service
- ✅ Booking status must be PENDING
- ✅ Check you're logged in as correct provider

---

### Payment/Earning Issues

**Problem**: "My earnings not showing"
- ✅ Bookings must have status = PAID
- ✅ Must click "Confirm Payment" button
- ✅ Only paid bookings count toward earnings
- ✅ Check you marked them as PAID

**Problem**: "Cannot mark as paid"
- ✅ Booking must be in CONFIRMED status first
- ✅ Parent must have paid you
- ✅ Check booking status

---

### Admin Issues

**Problem**: "Cannot access admin panel"
- ✅ You must be admin/staff user
- ✅ Ask system administrator
- ✅ User account must have is_staff = True
- ✅ Check you're logged in with admin account

**Problem**: "User showing in wrong role"
- ✅ Roles cannot be changed after registration
- ✅ User must create new account with correct role
- ✅ Or admin can deactivate old account

---

## Test Accounts (Sample Data)

After running default services setup:

### Test Parents
Create your own parent account to test

### Test Providers
```
Email: sarah.nanny@example.com
Password: (set during import)

Email: jessica.babysitter@example.com
Password: (set during import)

Email: michael.tutor@example.com
Password: (set during import)

Email: emma.childcare@example.com
Password: (set during import)
```

### Admin Account
```
Email: admin@example.com
Password: (from admin setup)
URL: /admin/
```

---

## Complete Workflow Examples

### Example 1: Parent Booking a Service (Start to Finish)

1. **Register**
   - Go to Register page
   - Choose "Parent" role
   - Fill all fields
   - Click Register
   - See: "Registration successful!"

2. **Login**
   - Go to Login page
   - Enter email and password
   - Click Login
   - See your name in top-right

3. **Browse Services**
   - Click "Services" menu
   - Search by location or view all
   - Click on service card
   - Review details, provider, availability

4. **Book Service**
   - Click "📚 Book Now" button
   - See: "Booking sent successfully!"
   - Check "My Bookings"
   - Status: 🟡 PENDING

5. **Wait for Confirmation**
   - (1-24 hours) Provider confirms
   - Status changes: 🟡 → 🟢 CONFIRMED
   - Check Inbox to chat with provider
   - Conversation auto-created

6. **Send Payment**
   - Contact provider via chat
   - Send payment details
   - Wait for confirmation

7. **Mark as Paid**
   - Provider clicks "Confirm Payment"
   - Status: 🟢 → ⚫ PAID
   - Download invoice from "My Bookings"
   - Booking complete!

---

### Example 2: Provider Setup (Start to Finish)

1. **Register**
   - Go to Register page
   - Choose "Provider" role
   - Fill all fields
   - Click Register
   - See: "Registration successful!"

2. **Login**
   - Go to Login page
   - Enter email and password
   - Click Login
   - See your name in top-right

3. **Add Service**
   - Click "Add Service" in profile menu
   - Fill: Title, Description, Location, Rate
   - Upload image (optional)
   - Click "Add Service"
   - See: "Service created successfully!"

4. **Manage Availability**
   - Click "Provider Dashboard"
   - Find your service
   - Click "📅 Manage Availability"
   - Block dates you're not available
   - Click "Save"

5. **Wait for Bookings**
   - Parents start booking your service
   - Dashboard shows 🟡 PENDING bookings

6. **Confirm Bookings**
   - Review parent info
   - Click "✅ Confirm" button
   - Status: 🟡 → 🟢 CONFIRMED
   - Parent gets notified
   - Chat opens

7. **Communicate with Parent**
   - Click "Inbox"
   - Find parent conversation
   - Send/receive messages
   - Confirm details, time, payment

8. **Mark as Paid**
   - After service provided
   - Parent sends payment
   - Click "💰 Confirm Payment"
   - Status: 🟢 → ⚫ PAID
   - Earning added to total

9. **View Earnings**
   - Go to "Provider Dashboard"
   - See total earnings
   - See monthly breakdown
   - Track income

---

## Quick Reference Commands

### Start Application
```bash
cd babycare
python manage.py runserver
```

### Access Locally
- Main app: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Register: http://127.0.0.1:8000/register/
- Login: http://127.0.0.1:8000/login/
- Services: http://127.0.0.1:8000/services/
- Dashboard: http://127.0.0.1:8000/provider-dashboard/
- My Bookings: http://127.0.0.1:8000/parent-bookings/
- Inbox: http://127.0.0.1:8000/inbox/

---

**Last Updated**: April 14, 2026
**Version**: 1.0 Complete
**Support**: Contact development team for issues

