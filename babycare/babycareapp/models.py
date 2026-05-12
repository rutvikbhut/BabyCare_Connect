from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.conf import settings


# Custom User Model (defined first since other models depend on it)
class User(AbstractUser):
    IS_PARENT = 'parent'
    IS_PROVIDER = 'provider'
    IS_ADMIN = 'admin'
    
    ROLE_CHOICES = [
        (IS_PARENT, 'Parent'),
        (IS_PROVIDER, 'Childcare Provider'),
        (IS_ADMIN, 'Admin'),
    ]
    
    # Override email field to make it unique (required for USERNAME_FIELD)
    email = models.EmailField(unique=True)
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=IS_PARENT)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    last_activity = models.DateTimeField(null=True, blank=True)
    is_typing = models.BooleanField(default=False)
    typing_to = models.IntegerField(null=True, blank=True)
    
    # Set email as the username field for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def is_online(self):
        if self.last_activity:
            # Consider online if active in the last 5 minutes
            from django.utils import timezone
            now = timezone.now()
            return now < self.last_activity + timezone.timedelta(minutes=5)
        return False

    def __str__(self):
        return f"{self.email} ({self.role})"


# Legacy model - Keep for backward compatibility
class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='parent')
    
    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email if self.user else "Unknown"

class Service(models.Model):
    provider = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'provider'}
    )
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)
    def save(self, *args, **kwargs):
        # 1. Save the record first so the file exists on disk
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # 2. Check if the image is larger than 800px
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                # 3. Resize and sharpen
                img.thumbnail(output_size, Image.Resampling.LANCZOS)
                img.save(self.image.path)


    title = models.CharField(max_length=200) # e.g., "Full-time Nanny"
    description = models.TextField(blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.provider.username}"

class Booking(models.Model):
    parent = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'parent'}
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    start_date = models.DateField()
    status = models.CharField(
        max_length=20, 
        choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('paid', 'Paid')],
        default='pending'
    )


class Availability(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='unavailability')
    date = models.DateField()
    reason = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ('service', 'date')

    def __str__(self):
        return f"{self.service.title} unavailable on {self.date}"



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender.first_name} to {self.receiver.first_name}"