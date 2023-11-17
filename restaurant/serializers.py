from rest_framework import serializers
from .models import Booking, MenuItem, Table
from django.contrib.auth.models import User


# class MenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Menu
#         fields= '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
