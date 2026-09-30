from django.db import models

from turf.models import Turf
# Create your models here.

class Booking(models.Model):

    customer_name = models.CharField(max_length=200)

    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)

    booking_date = models.DateField()

    booking_time = models.TimeField()

    duration = models.IntegerField()

    phone_number = models.IntegerField()

    email = models.EmailField()
    