from django.urls import path
from .views import *

urlpatterns = [
    path('', employee_login, name='employee_login'),
    path('Dashboard', employee_dashboard, name='employee_dashboard'),
    path('api/checkin/', checkin, name='checkin'),
    path('checkout/', checkout, name='checkout'),
]
