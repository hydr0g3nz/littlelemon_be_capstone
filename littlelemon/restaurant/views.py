from rest_framework import viewsets, permissions
from .models import Booking, Menu
from .serializers import BookingSerializer , MenuSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

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

class MenuViewSet(viewsets.ViewSet):
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self, request):
        serializer =MenuSerializer(data=request.data ,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        menu = Menu.objects.all()
        serializer= MenuSerializer(menu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        menus = Menu.objects.all()
        menu = get_object_or_404(menus,pk=pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)