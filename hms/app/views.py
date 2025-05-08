from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Appointment
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Diagnosis

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('patient')  # Change this to your desired home/dashboard page
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')

@csrf_exempt
def book_appointment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        phone = data.get('phone')
        message = data.get('message')
        date = data.get('date')
        shift = data.get('shift')

        # Count existing appointments for the same date and shift
        existing_tokens = Appointment.objects.filter(date=date, shift=shift).count()
        
        if existing_tokens >= 100:
            return JsonResponse({'success': False, 'error': 'Token limit (1-100) reached for this shift and date.'}, status=400)
        
        token = existing_tokens + 1

        appointment = Appointment.objects.create(
            name=name,
            phone=phone,
            message=message,
            date=date,
            shift=shift,
            token=token
        )

        return JsonResponse({
            'success': True,
            'token': token,
            'name': appointment.name,
            'date': appointment.date,
        })

    return JsonResponse({'success': False}, status=400)
def home(request):
    return render(request , 'home.html')
def about(request):
    return render(request , 'about.html')
def library(request):
    return render(request , 'library.html')
@login_required
def patient(request):
    records = Diagnosis.objects.filter(patient=request.user)
    return render(request , 'patient.html', {'records': records})
# Create your views here.
@login_required
def appointment(request):
    records = Diagnosis.objects.filter(patient=request.user)
    return render(request , 'appointment.html', {'records': records})

def admin_patient(request):
    return render(request, 'admin_patient')