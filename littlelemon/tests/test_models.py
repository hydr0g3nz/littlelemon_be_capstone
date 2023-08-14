from django.test import TestCase
from restaurant.models import Booking
from django.contrib.auth.models import User
class BookingTest(TestCase):
    def test_get_item(self):
        user = User.objects.create_user(username='testuser', password='testpassword')

        item = Booking.objects.create(user = user,booking_date = '2023-08-14',no_of_guests= 2)
        self.assertEqual(str(item),"testuser 2023-08-14 2")