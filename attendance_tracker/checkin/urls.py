from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),  # Connect the UI
    path('checkin/', checkin, name='checkin'),
    path('checkout/', checkout, name='checkout'),
]
