# define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'username', 'password')

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Booking
        fields = ["user", "booking_date", "no_of_guests"]

       
