from rest_framework import viewsets, permissions
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserCreateSerializer

class BookingViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = BookingSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        bookings = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

