from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail, EmailMessage
from django.db import models
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template, render_to_string
from rest_framework.response import Response
from rest_framework.decorators import api_view
from xhtml2pdf import pisa
from io import BytesIO
import re
from datetime import datetime

from .models import User, register, contact, LoginHistory, Service, Booking, Availability, Message
from .serialize_ import user_serializer
# Create your views here.

# Email validation function
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None



def home(request):
    #  if not request.session.get('user_id'):
    #     return redirect('login')
    return render(request, 'babycareapp/index.html')

def about(request):
    return render(request, 'babycareapp/about.html')

def register_(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        repassword = request.POST.get('repassword', '')
        role = request.POST.get('role', 'parent')
        terms = request.POST.get('terms')  

        # Check for empty inputs first
        if not name:
            return render(request, 'babycareapp/register.html', {'error': 'Please enter your name'})
        
        if len(name) < 2:
            return render(request, 'babycareapp/register.html', {'error': 'Name must be at least 2 characters'})
            
        if not email:
            return render(request, 'babycareapp/register.html', {'error': 'Please enter your email'})
        
        if not is_valid_email(email):
            return render(request, 'babycareapp/register.html', {'error': 'Please enter a valid email address'})
            
        if not password:
            return render(request, 'babycareapp/register.html', {'error': 'Please enter a password'})
        
        if len(password) < 6:
            return render(request, 'babycareapp/register.html', {'error': 'Password must be at least 6 characters'})
            
        if not repassword:
            return render(request, 'babycareapp/register.html', {'error': 'Please confirm your password'})
        
        if not terms:
            return render(request, 'babycareapp/register.html', {'error': 'Please agree to the Terms of Service'})
        
        if password != repassword:
            return render(request, 'babycareapp/register.html', {'error': 'Passwords do not match'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'babycareapp/register.html', {'error': 'Email is already registered'})
        
        try:
            # Create user with Django's built-in User model
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=name
            )
            user.role = role
            user.save()

            try:
                send_mail(
                    "Welcome to BabyCare Connect",
                    f"Hello {name},\n\nWelcome to BabyCare Connect! Your account has been created successfully.\n\nBest regards,\nBabyCare Connect Team",
                    "rutvikbhut920@gmail.com",
                    [email],    
                    fail_silently=False
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            
            messages.success(request, "Registration successful! Please login.")
            return redirect('login')
        except Exception as e:
            print(f"Registration error: {e}")
            return render(request, 'babycareapp/register.html', {'error': f'Registration failed. Please try again.'})

    return render(request, 'babycareapp/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        # Validate input
        if not email:
            return render(request, 'babycareapp/login.html', {'error_login': 'Please enter your email'})
        
        if not is_valid_email(email):
            return render(request, 'babycareapp/login.html', {'error_login': 'Please enter a valid email address'})
            
        if not password:
            return render(request, 'babycareapp/login.html', {'error_login': 'Please enter your password'})

        # Authenticate using EmailBackend (passes email as username)
        user = authenticate(request, username=email, password=password)

        if user is not None:
            django_login(request, user)  # Login first to rotate session ID
            
            # Now set session variables after login
            request.session['email'] = user.email 
            request.session['role'] = user.role
            request.session['user_id'] = user.id
            request.session['user_name'] = user.first_name if user.first_name else user.email.split('@')[0]
            
            # Record login in LoginHistory
            try:
                LoginHistory.objects.create(
                    user=user,
                    is_active=True
                )
            except Exception as e:
                print(f"Error recording login: {e}")
            
            # Check for 'next' parameter in URL
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)

            # Redirect based on Role
            if user.role == 'provider':
                messages.success(request, f"Welcome back, {user.first_name}!")
                return redirect('provider_dashboard')
            elif user.role == 'admin':
                messages.success(request, f"Welcome back, Admin {user.first_name}!")
                return redirect('admin_dashboard')
            else:
                messages.success(request, f"Welcome back, {user.first_name}!")
                return redirect('service_list')
        else:
            return render(request, 'babycareapp/login.html', {
                'error_login': 'Invalid email or password'
            })

    return render(request, 'babycareapp/login.html')

def logout_view(request):
    if request.user.is_authenticated:
        # Record logout in LoginHistory
        try:
            login_record = LoginHistory.objects.filter(
                user=request.user, 
                is_active=True
            ).order_by('-login_time').first()
            
            if login_record:
                login_record.logout_time = timezone.now()
                login_record.is_active = False
                login_record.save()
        except Exception as e:
            print(f"Error recording logout: {e}")
        
        user_name = request.user.first_name or request.user.email
        messages.success(request, f"Goodbye {user_name}! You have been logged out successfully.")
    
    django_logout(request)
    request.session.flush()
    return redirect('home')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        # Validation
        errors = []
        if not name or len(name) < 2:
            errors.append('Please enter a valid name')
        if not email or not is_valid_email(email):
            errors.append('Please enter a valid email')
        if not subject or len(subject) < 3:
            errors.append('Please enter a valid subject')
        if not message_text or len(message_text) < 10:
            errors.append('Message must be at least 10 characters')
        
        if errors:
            return render(request, 'babycareapp/contact.html', {'errors': errors})

        try:
            # Save the contact message to the database
            contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text
            )
            
            # Send confirmation email
            try:
                send_mail(
                    f"We received your message: {subject}",
                    f"Hi {name},\n\nThank you for contacting BabyCare Connect. We received your message and will get back to you soon.\n\nBest regards,\nBabyCare Connect Team",
                    "rutvikbhut920@gmail.com",
                    [email],
                    fail_silently=True
                )
            except:
                pass
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        except Exception as e:
            return render(request, 'babycareapp/contact.html', {'error': f'Failed to send message: {str(e)}'})
    
    return render(request, 'babycareapp/contact.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        new_password = request.POST.get('new_password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # ✅ VALIDATION
        if not email or not new_password or not confirm_password:
            return render(request, 'babycareapp/forgot_password.html', {
                'error': 'Please fill all fields'
            })

        if new_password != confirm_password:
            return render(request, 'babycareapp/forgot_password.html', {
                'error': 'Passwords do not match'
            })

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)  # ✅ Properly hashes password
            user.save()

            return render(request, 'babycareapp/forgot_password.html', {
                'success': 'Password reset successful. You can login now.'
            })

        except User.DoesNotExist:
            return render(request, 'babycareapp/forgot_password.html', {
                'error': 'Email not registered'
            })

    return render(request, 'babycareapp/forgot_password.html')


@api_view(['GET'])  
def api_test(request):
    return Response({
        '1':"one",
        '2':"two"})

@api_view(['GET'])  
def api_user(request):
    users = User.objects.all()
    serialize_user = user_serializer(users, many=True)
    return Response(serialize_user.data)

@api_view(['POST'])
def api_store_data(request):
    serialize_user = user_serializer(data=request.data)
    if serialize_user.is_valid():
        serialize_user.save()
        return Response("data stored successfully")
    else:
        return Response("data is not valid")
    
# @api_view(['PUT'])
# def api_update_data(request, pk):
#     old_data= register.objects.get(name='rutvik')
#     serialize_user = user_serializer(old_data, data=request.data)
#     if serialize_user.is_valid():
#         serialize_user.save()
#         return Response("data updated successfully")
#     else:
#         return Response("data is not valid")
    

# @api_view(['PATCH'])
# def api_update_data(request,id):
#     old_data= register.objects.get(name=id)
#     serialize_user = user_serializer(old_data, data=request.data, partial=True)
#     if serialize_user.is_valid():
#         serialize_user.save()
#         return Response("data updated successfully")
#     else:
#         return Response("data is not valid")

# @api_view(['DELETE'])
# def delete_data(request, id):
#     data_to_delete = request.GET.get('term')
#     reg = register.objects.get(id=data_to_delete)
#     reg.delete()
#     return Response("data deleted successfully") 

def service_list(request):
    # Get the search query from the URL (e.g., ?q=New+York)
    query = request.GET.get('q', '').strip()
    
    if query:
        # Filter services where the location contains the search term (case-insensitive)
        services = Service.objects.filter(
            location__icontains=query, 
            is_available=True
        ).order_by('-id')
    else:
        # If no search, show all available services
        services = Service.objects.filter(is_available=True).order_by('-id')
    
    return render(request, 'babycareapp/service_list.html', {
        'services': services,
        'query': query
    })

@login_required
def create_booking(request, service_id):
    # 1. Get the specific service the parent clicked    
    service = get_object_or_404(Service, id=service_id)
    
    # 2. Check if the user is a Parent (and not a Provider booking themselves)
    if not hasattr(request.user, 'role') or request.user.role != 'parent':
        messages.error(request, "Only parents can book services.")
        return redirect('service_list')

    # 3. Check if already booked
    if Booking.objects.filter(parent=request.user, service=service, status__in=['pending', 'confirmed']).exists():
        messages.warning(request, "You already have a pending booking for this service.")
        return redirect('service_detail', service_id=service.id)

    # 4. Create the booking record with current date
    booking = Booking.objects.create(
        parent=request.user,
        service=service,
        start_date=timezone.now().date(),
        status='pending'
    )
    
    # 5. Create an initial message to start the conversation
    try:
        Message.objects.create(
            sender=request.user,
            receiver=service.provider,
            service=service,
            content=f"Hello! I'm interested in booking your '{service.title}' service. Please review my request."
        )
    except Exception as e:
        print(f"Error creating initial message: {e}")
    
    messages.success(request, f"✓ Booking request for '{service.title}' sent successfully! Waiting for provider confirmation.")
    return redirect('service_detail', service_id=service.id)


@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required
def provider_dashboard(request):
    # Ensure the user is a provider
    if not hasattr(request.user, 'role') or request.user.role != 'provider':
        messages.error(request, 'Only providers can access this dashboard.')
        return redirect('service_list')

    provider = request.user

    # Get all provider services
    services = Service.objects.filter(provider=provider).order_by('-id')
    
    # Get provider bookings (all, not just paid)
    my_bookings = Booking.objects.filter(service__provider=provider).order_by('-id')
    
    # Calculate total earnings from paid bookings only
    total_earnings = Booking.objects.filter(
        service__provider=provider, 
        status='paid'
    ).aggregate(total=Sum('service__hourly_rate'))['total'] or 0

    # Monthly Report Logic
    monthly_report = Booking.objects.filter(
        service__provider=provider, 
        status='paid'
    ).annotate(
        month=TruncMonth('start_date')
    ).values('month').annotate(
        total_monthly=Sum('service__hourly_rate'),
        count=Count('id')
    ).order_by('-month')

    # Add 'net_pay' attribute to each booking (90% after 10% commission)
    for booking in my_bookings:
        booking.net_pay = float(booking.service.hourly_rate) * 0.90

    return render(request, 'babycareapp/provider_dashboard.html', {
        'user': provider,
        'services': services,
        'bookings': my_bookings,
        'provider': provider,
        'total_earnings': total_earnings,
        'monthly_report': monthly_report,
    })

@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required
def update_booking_status(request, booking_id, status):
    booking = get_object_or_404(Booking, id=booking_id, service__provider=request.user)
    booking.status = status
    booking.save()
    messages.success(request, f"Booking updated to {status}.")
    return redirect('provider_dashboard')

@login_required
def parent_bookings(request):
    if not hasattr(request.user, 'role') or request.user.role != 'parent':
        messages.error(request, 'Only parents can view their bookings.')
        return redirect('service_list')
    
    # Get all bookings made by this parent, ordered by most recent
    bookings = Booking.objects.filter(parent=request.user).order_by('-id')
    return render(request, 'babycareapp/parent_bookings.html', {'bookings': bookings})

@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required
def mark_as_paid(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, service__provider=request.user)
    
    if booking.status == 'paid':
        messages.warning(request, "This booking is already marked as paid.")
        return redirect('provider_dashboard')
    
    booking.status = 'paid'
    booking.save()
    
    # Automatically send the email
    try:
        send_invoice_email(booking)
        messages.success(request, "Payment confirmed and receipt emailed to parent!")
    except Exception as e:
        print(f"Error sending invoice: {e}")
        messages.warning(request, "Payment confirmed, but email failed to send.")

    return redirect('provider_dashboard')

@login_required
def add_service(request):
    if not hasattr(request.user, 'role') or request.user.role != 'provider':
        messages.error(request, 'Only providers can add services.')
        return redirect('service_list')

    if request.method == 'POST':
        # Capture text and files
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        hourly_rate = request.POST.get('hourly_rate', '').strip()
        location = request.POST.get('location', '').strip()
        service_image = request.FILES.get('image')

        # Validation
        errors = []
        if not title or len(title) < 3:
            errors.append('Service title must be at least 3 characters')
        if not location or len(location) < 3:
            errors.append('Location must be at least 3 characters')
        if not hourly_rate:
            errors.append('Hourly rate is required')
        else:
            try:
                rate = float(hourly_rate)
                if rate <= 0:
                    errors.append('Hourly rate must be greater than 0')
            except ValueError:
                errors.append('Hourly rate must be a valid number')

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'babycareapp/add_service.html')

        try:
            Service.objects.create(
                provider=request.user,
                title=title,
                description=description if description else '',
                hourly_rate=float(hourly_rate),
                location=location,
                image=service_image
            )

            messages.success(request, "Service listed successfully!")
            return redirect('provider_dashboard')
        except Exception as e:
            messages.error(request, f'Failed to create service: {str(e)}')
            return render(request, 'babycareapp/add_service.html')

    return render(request, 'babycareapp/add_service.html')


@login_required
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def user_profile(request):
    """Display user profile with all information"""
    user = request.user
    
    # If parent, get their bookings
    if user.role == 'parent':
        bookings = Booking.objects.filter(parent=user).count()
        context = {
            'user': user,
            'total_bookings': bookings,
        }
    # If provider, get their services and earnings
    elif user.role == 'provider':
        services = Service.objects.filter(provider=user).count()
        total_earnings = Booking.objects.filter(
            service__provider=user,
            status='paid'
        ).aggregate(total=Sum('service__hourly_rate'))['total'] or 0
        
        context = {
            'user': user,
            'total_services': services,
            'total_earnings': total_earnings,
        }
    else:
        context = {'user': user}
    
    return render(request, 'babycareapp/user_profile.html', context)


@login_required
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def edit_profile(request):
    """Edit user profile information"""
    user = request.user
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        address = request.POST.get('address', '').strip()
        
        # Validation
        if not first_name:
            messages.error(request, 'First name is required')
            return redirect('user_profile')
        
        if len(first_name) < 2:
            messages.error(request, 'First name must be at least 2 characters')
            return redirect('user_profile')
        
        # Update user information
        try:
            user.first_name = first_name
            user.last_name = last_name
            user.phone_number = phone_number
            user.address = address
            user.save()
            
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_profile')
        except Exception as e:
            messages.error(request, f'Error updating profile: {str(e)}')
            return redirect('user_profile')
    
    return render(request, 'babycareapp/edit_profile.html', {'user': user})


def service_detail(request, service_id):
    # Fetch the specific service or return a 404 error if not found
    service = get_object_or_404(Service, id=service_id)
    blocked_dates = Availability.objects.filter(service=service).values_list('date', flat=True)
    
    return render(request, 'babycareapp/service_detail.html', {
        'service': service,
        'blocked_dates': blocked_dates
    })


@login_required
def manage_availability(request, service_id):
    service = get_object_or_404(Service, id=service_id, provider=request.user)
    
    if request.method == 'POST':
        date_str = request.POST.get('date', '').strip()
        
        if not date_str:
            messages.error(request, 'Please select a date')
            return redirect('manage_availability', service_id=service.id)
        
        try:
            # Validate date format
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            
            # Don't allow past dates
            if date_obj < timezone.now().date():
                messages.error(request, 'Cannot block dates in the past')
                return redirect('manage_availability', service_id=service.id)
            
            Availability.objects.get_or_create(service=service, date=date_obj)
            messages.success(request, f"Date {date_obj} is now marked as unavailable.")
        except ValueError:
            messages.error(request, 'Invalid date format')
        
        return redirect('manage_availability', service_id=service.id)

    unavailable_dates = Availability.objects.filter(service=service).order_by('date')
    return render(request, 'babycareapp/manage_availability.html', {
        'service': service,
        'unavailable_dates': unavailable_dates,
        'today_date': timezone.now().date()
    })





#chat
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required
def inbox(request):
    """Display list of users the current user has messaged"""
    # Get all messages involving this user
    conversations = Message.objects.filter(
        models.Q(sender=request.user) | models.Q(receiver=request.user)
    ).values('sender', 'receiver').distinct()
    
    # Build list of unique conversation partners
    partners = set()
    for conv in conversations:
        sender_id = conv['sender']
        receiver_id = conv['receiver']
        
        # Add sender if not the current user
        if sender_id != request.user.id:
            try:
                user = User.objects.get(id=sender_id)
                partners.add(user)
            except User.DoesNotExist:
                pass
        
        # Add receiver if not the current user
        if receiver_id != request.user.id:
            try:
                user = User.objects.get(id=receiver_id)
                partners.add(user)
            except User.DoesNotExist:
                pass
    
    # Count unread messages for this user
    unread_count = Message.objects.filter(receiver=request.user, is_read=False).count()
    
    # Sort partners by most recent message
    partners_list = list(partners)
    partners_list.sort(
        key=lambda p: Message.objects.filter(
            models.Q(sender=request.user, receiver=p) | 
            models.Q(sender=p, receiver=request.user)
        ).order_by('-timestamp').first().timestamp if Message.objects.filter(
            models.Q(sender=request.user, receiver=p) | 
            models.Q(sender=p, receiver=request.user)
        ).exists() else timezone.now(),
        reverse=True
    )
    
    return render(request, 'babycareapp/inbox.html', {
        'partners': partners_list,
        'unread_count': unread_count
    })

@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required
def chat_room(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    
    # Mark all messages FROM this receiver TO the current user as READ
    Message.objects.filter(sender=receiver, receiver=request.user, is_read=False).update(is_read=True)
    
    # Fetch all messages between these two users
    messages_list = Message.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver=receiver)) |
        (models.Q(sender=receiver) & models.Q(receiver=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return redirect('chat_room', receiver_id=receiver.id)

    return render(request, 'babycareapp/chat.html', {
        'receiver': receiver,
        'chat_messages': messages_list
    })



@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def check_unread_api(request):
    if request.user.is_authenticated:
        # Get the most recent unread message
        latest = Message.objects.filter(receiver=request.user, is_read=False).last()
        if latest:
            return JsonResponse({
                'new_message': True,
                'sender': latest.sender.first_name,
                'text': latest.content[:50] + "..." # Snippet of the message
            })
    return JsonResponse({'new_message': False})



# Only allow users with 'admin' role to see this
@user_passes_test(lambda u: hasattr(u, 'role') and u.role == 'admin')
def admin_dashboard(request):
    # 1. User Statistics
    total_parents = User.objects.filter(role='parent').count()
    total_providers = User.objects.filter(role='provider').count()
    total_admins = User.objects.filter(role='admin').count()
    
    # 2. Booking Statistics
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(status='pending').count()
    confirmed_bookings = Booking.objects.filter(status='confirmed').count()
    paid_bookings = Booking.objects.filter(status='paid').count()
    
    # 3. Financial Statistics (Total platform volume)
    total_revenue = Booking.objects.filter(status='paid').aggregate(
        total=Sum('service__hourly_rate')
    )['total'] or 0

    # 4. Top Services (Most booked)
    top_services = Service.objects.annotate(
        num_bookings=Count('booking')
    ).order_by('-num_bookings')[:5]

    # 5. Calculate Total Transaction Volume
    total_volume = Booking.objects.filter(status='paid').aggregate(
        total=Sum('service__hourly_rate')
    )['total'] or 0

    # 6. Calculate Platform Profit (10% Commission)
    commission_rate = 0.10
    total_profit = float(total_volume) * commission_rate

    return render(request, 'babycareapp/admin_dashboard.html', {
        'total_parents': total_parents,
        'total_providers': total_providers,
        'total_admins': total_admins,
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'confirmed_bookings': confirmed_bookings,
        'paid_bookings': paid_bookings,
        'total_revenue': total_revenue,
        'top_services': top_services,
        'total_volume': total_volume,
        'total_profit': total_profit,
        'commission_percent': commission_rate * 100
    })



@login_required
def view_invoice(request, booking_id):
    # 1. Get the booking (ensure it's paid and belongs to parent)
    booking = get_object_or_404(Booking, id=booking_id, status='paid', parent=request.user)
    
    # 2. Setup the data for the invoice
    hours = 1
    amount = booking.service.hourly_rate * hours
    
    context = {
        'booking': booking,
        'amount': amount,
        'hours': hours,
        'date': booking.start_date,
    }
    
    return render(request, 'babycareapp/view_invoice.html', context)

def download_invoice(request, booking_id):
    # 1. Get the booking (ensure it's paid and belongs to parent)
    booking = get_object_or_404(Booking, id=booking_id, status='paid', parent=request.user)
    
    # 2. Setup the data for the template (default 1 hour)
    hours = 1
    amount = booking.service.hourly_rate * hours
    
    context = {
        'booking': booking,
        'amount': amount,
        'hours': hours,
        'date': booking.start_date,
    }
    
    try:
        # 3. Render the HTML template into a PDF
        template = get_template('babycareapp/invoice_pdf.html')
        html = template.render(context)
        result = BytesIO()
        
        # Create the PDF
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        
        if not pdf.err:
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="Invoice_{booking_id}.pdf"'
            return response
        else:
            return HttpResponse("Error generating PDF", status=400)
    except Exception as e:
        print(f"PDF generation error: {e}")
        return HttpResponse(f"Error generating PDF: {str(e)}", status=500)



def send_invoice_email(booking):
    # 1. Setup the data for invoice (default 1 hour)
    hours = 1
    amount = booking.service.hourly_rate * hours
    
    # 2. Prepare context for the HTML
    context = {
        'booking': booking,
        'amount': amount,
        'hours': hours,
        'date': booking.start_date,
    }
    
    # 3. Render the HTML for the PDF
    html_content = render_to_string('babycareapp/invoice_pdf.html', context)
    
    # 4. Generate the PDF in memory
    pdf_main = BytesIO()
    pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), pdf_main)
    
    # 5. Create and send the Email
    subject = f"Receipt for your booking #{booking.id}"
    body = f"Hi {booking.parent.first_name}, thank you for your payment for {booking.service.title}. Please find your receipt attached."
    email = EmailMessage(subject, body, 'noreply@babycareconnect.com', [booking.parent.email])
    
    # 6. Attach the PDF
    email.attach(f'Invoice_{booking.id}.pdf', pdf_main.getvalue(), 'application/pdf')
    email.send()


@login_required
@login_required
def update_typing_status(request):
    is_typing = request.GET.get('typing') == 'true'
    receiver_id = request.GET.get('receiver_id')
    
    User.objects.filter(id=request.user.id).update(
        is_typing=is_typing, 
        typing_to=int(receiver_id) if is_typing and receiver_id else None
    )
    return JsonResponse({'status': 'updated'})

@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required
def check_typing_status(request, receiver_id):
    # Check if the person I am talking to is typing to ME
    other_user = get_object_or_404(User, id=receiver_id)
    is_typing = other_user.is_typing and other_user.typing_to == request.user.id
    return JsonResponse({'is_typing': is_typing})