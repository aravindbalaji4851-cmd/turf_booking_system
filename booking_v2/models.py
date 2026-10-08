from django.db import models

from turf.models import Turf
# Create your models here.


class Slots(models.Model):

    customer_name = models.CharField(max_length=200)
    
    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)
    
    booking_date = models.DateField()
    
    start_time = models.TimeField()
    
    duration = models.DurationField()

    end_time = models.TimeField(null=True)
    
    phone_number = models.IntegerField()
    
    email = models.EmailField()