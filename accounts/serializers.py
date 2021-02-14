from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Customer, Staff

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','username','email']
        model = Customer

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','username','email']
        model = Staff