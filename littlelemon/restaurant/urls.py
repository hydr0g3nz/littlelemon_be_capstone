from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet,MenuViewSet

router1 = DefaultRouter()
router1.register(r"tables", BookingViewSet, basename="tables")

router2 = DefaultRouter()
router2.register(r'menu',MenuViewSet,basename='menus')
urlpatterns = [
 
    path("booking/", include(router1.urls)),
    path("",include(router2.urls)),
]
