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

class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50, null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return self.name