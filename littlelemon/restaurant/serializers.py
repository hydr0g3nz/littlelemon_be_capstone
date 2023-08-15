# define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking,Menu
from rest_framework import serializers



class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Booking
        fields = ["user", "booking_date", "no_of_guests"]

       
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields="__all__"