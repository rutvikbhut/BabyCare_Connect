from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact_us, name='contact'),
    path('about/', views.about, name='about'),

    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('api_test/', views.api_test, name='api_test'),
    path('api_user/', views.api_user, name='api_user'),
    path('api_store_data/', views.api_store_data, name='api_store_data'),

    path('services/', views.service_list, name='service_list'), 
    path('book/<int:service_id>/', views.create_booking, name='create_booking'),
    path('provider_dashboard/', views.provider_dashboard, name='provider_dashboard'),
    path('update-booking/<int:booking_id>/<str:status>/', views.update_booking_status, name='update_status'),

    path('my-bookings/', views.parent_bookings, name='parent_bookings'),
    path('mark-paid/<int:booking_id>/', views.mark_as_paid, name='mark_paid'),
    path('add-service/', views.add_service, name='add_service'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('manage-availability/<int:service_id>/', views.manage_availability, name='manage_availability'),
    path('inbox/', views.inbox, name='inbox'),
    path('chat/<int:receiver_id>/', views.chat_room, name='chat_room'),
    path('api/check-unread/', views.check_unread_api, name='check_unread_api'),
    path('admin-stats/', views.admin_dashboard, name='admin_dashboard'),
    path('booking/invoice/<int:booking_id>/view/', views.view_invoice, name='view_invoice'),
    path('booking/invoice/<int:booking_id>/download/', views.download_invoice, name='download_invoice'),
    path('update-typing/', views.update_typing_status, name='update_typing'),
    path('check-typing/<int:receiver_id>/', views.check_typing_status, name='check_typing'),

    # path('api_update_data/<int:id>/', api_update_data, name='api_update_data'),
    # path('accounts/', include('allauth.urls')),
    
]