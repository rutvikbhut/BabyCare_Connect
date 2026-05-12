from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

User = get_user_model()

# Signals can be added here when needed for User model events
# For now, keeping this file for future use