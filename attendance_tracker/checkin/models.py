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


class Department(models.Model):
    department_name = models.CharField(max_length=50)
    description =models.TextField()
    location = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.CharField(max_length=50,null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50,null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return self.department_name

class Role(models.Model):
    name = models.CharField(max_length=50)
    description =models.TextField()
    created_by = models.CharField(max_length=50,null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50,null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.CharField(max_length=50,null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50,null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return self.name
