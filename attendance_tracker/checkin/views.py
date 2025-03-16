
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.timezone import now
from .models import CheckInRecord
from django.contrib.auth.models import User
from geopy.distance import geodesic
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

# Set office coordinates (latitude, longitude)
OFFICE_LOCATION = (11.0420173, 76.9758697)


def employee_login(request):
    if request.method == 'POST':
        return redirect('employee_dashboard')
    return render(request, 'Login/index.html')

def employee_dashboard(request):
    if request.method == 'POST':
        return redirect('employee_dashboard')
    return render(request, 'Dashboard/dashboard.html')


@api_view(['POST'])
# @permission_classes([IsAuthenticated]) 
def checkin(request):
    # user = request.user
    latitude = float(request.data.get('latitude'))
    longitude = float(request.data.get('longitude'))
    user_location = (latitude, longitude)
    print(user_location)
    
    # Calculate distance
    distance = geodesic(OFFICE_LOCATION, user_location).meters
    
    if distance > 50:  # Allow check-in only within 50 meters
        return Response({'message': 'You are too far from the office to check in!'}, status=400)
    
    checkin_record = CheckInRecord.objects.create(
        # employee=user,
        latitude=latitude,
        longitude=longitude
    )
    return Response({'message': 'Checked in successfully!', 'time': checkin_record.checkin_time})



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def checkout(request):
    user = request.user
    try:
        checkin_record = CheckInRecord.objects.filter(employee=user).latest('checkin_time')
        if checkin_record.checkout_time:
            return Response({'message': 'Already checked out!'}, status=400)
        
        checkin_record.checkout_time = now()
        checkin_record.save()
        return Response({'message': 'Checked out successfully!', 'time': checkin_record.checkout_time})
    except CheckInRecord.DoesNotExist:
        return Response({'message': 'No check-in record found!'}, status=400)
