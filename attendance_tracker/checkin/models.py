from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class CheckInRecord(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    checkin_time = models.DateTimeField(default=now, blank=True)
    checkout_time = models.DateTimeField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    # def __str__(self):
    #     return f"{self.employee.username} - {self.checkin_time}"
