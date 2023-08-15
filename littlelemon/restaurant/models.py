from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    booking_date = models.DateField()
    no_of_guests = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.user} {self.booking_date} {self.no_of_guests}'


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.SmallIntegerField()