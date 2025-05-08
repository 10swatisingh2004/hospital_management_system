# admin.py
from django.contrib import admin
from .models import Appointment, Diagnosis
from .models import Bed, Patient , Employee

# Registering the models for the admin interface
@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ('bed_no', 'ventilator' , 'status' , 'diagnosis')
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age' , 'gender' , 'blood_group', 'diagnosis' , 'mobile' , 'admission_date' , 'discharge_date')
    search_fields = ('name', 'phone')  # search functionality for name and phone
# Register the Appointment model
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'date', 'shift', 'token', 'created_at')  # columns to display in the list view
    search_fields = ('name', 'phone','date')  # search functionality for name and phone

# Register the Diagnosis model
@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('id','patient', 'date', 'price', 'paid')  # columns to display in the list view
    search_fields = ('patient__username', 'symptoms')  # search functionality for patient's username and symptoms
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name' , 'gender' , 'date_of_birth' , 'designation' ,'date_of_joining' , 'shift')
    search_fields = ('name' , 'designation', 'shift')
