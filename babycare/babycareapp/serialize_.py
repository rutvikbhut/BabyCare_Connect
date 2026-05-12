from rest_framework import serializers
from .models import register

class user_serializer(serializers.ModelSerializer):
   class Meta:
    model = register
    #   fields = ['id', 'name', 'email']
    fields = '__all__'
   