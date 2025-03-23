from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)

@admin.register(CheckInRecord)
class CheckInRecordAdmin(admin.ModelAdmin):
    list_display = ('id','employee', 'checkin_time', 'latitude', 'longitude')  # Replace 'employee' with the actual field

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','department_name', 'description', 'location')
