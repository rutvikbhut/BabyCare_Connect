from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Register your models here.

# Custom User Admin
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'first_name', 'role', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'address')}),
        ('Role & Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Status', {'fields': ('is_typing', 'typing_to', 'last_activity')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'role'),
        }),
    )

admin.site.register(User, CustomUserAdmin)


# Legacy Register Model (for backward compatibility)
class registerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role', 'password')
    search_fields = ('name', 'email')
    list_filter = ('role',)
    readonly_fields = ('password',)  # Don't edit passwords in admin

admin.site.register(register, registerAdmin)


# Contact Admin
class contactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

admin.site.register(contact, contactAdmin)


# Login History Admin
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_email', 'login_time', 'logout_time', 'is_active')
    search_fields = ('user__email',)
    list_filter = ('is_active', 'login_time')
    readonly_fields = ('login_time', 'logout_time')
    
    def get_user_email(self, obj):
        return obj.user.email if obj.user else "User Deleted"
    get_user_email.short_description = 'User Email'

admin.site.register(LoginHistory, LoginHistoryAdmin)


# Service Admin
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_provider_email', 'location', 'hourly_rate', 'is_available')
    search_fields = ('title', 'location', 'provider__email')
    list_filter = ('is_available', 'location')
    
    def get_provider_email(self, obj):
        return obj.provider.email if obj.provider else "Unknown"
    get_provider_email.short_description = 'Provider'

admin.site.register(Service, ServiceAdmin)


# Booking Admin
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_parent_email', 'get_service_title', 'status', 'start_date')
    search_fields = ('parent__email', 'service__title')
    list_filter = ('status', 'start_date')
    readonly_fields = ('start_date',)
    
    def get_parent_email(self, obj):
        return obj.parent.email if obj.parent else "Unknown"
    get_parent_email.short_description = 'Parent'
    
    def get_service_title(self, obj):
        return obj.service.title if obj.service else "Unknown"
    get_service_title.short_description = 'Service'

admin.site.register(Booking, BookingAdmin)


# Availability Admin
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_service_title', 'date', 'get_provider')
    search_fields = ('service__title', 'service__provider__email')
    list_filter = ('date',)
    
    def get_service_title(self, obj):
        return obj.service.title if obj.service else "Unknown"
    get_service_title.short_description = 'Service'
    
    def get_provider(self, obj):
        return obj.service.provider.email if obj.service and obj.service.provider else "Unknown"
    get_provider.short_description = 'Provider'

admin.site.register(Availability, AvailabilityAdmin)


# Message Admin
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_sender_email', 'get_receiver_email', 'content_preview', 'timestamp', 'is_read')
    search_fields = ('sender__email', 'receiver__email', 'content')
    list_filter = ('timestamp', 'is_read')
    readonly_fields = ('timestamp',)
    
    def get_sender_email(self, obj):
        return obj.sender.email if obj.sender else "Unknown"
    get_sender_email.short_description = 'Sender'
    
    def get_receiver_email(self, obj):
        return obj.receiver.email if obj.receiver else "Unknown"
    get_receiver_email.short_description = 'Receiver'
    
    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Message'

admin.site.register(Message, MessageAdmin)



