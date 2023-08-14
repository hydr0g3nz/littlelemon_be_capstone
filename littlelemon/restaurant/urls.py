from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet

router = DefaultRouter()
router.register(r"tables", BookingViewSet, basename="tables")
urlpatterns = [
 
    path("booking/", include(router.urls)),
]
