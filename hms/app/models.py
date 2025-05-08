# models.py
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Appointment(models.Model):
    SHIFT_CHOICES = [
        ('first', '9am-12pm'),
        ('second', '1pm-3pm'),
        ('third', '4pm-6pm'),
    ]
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateField()
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    token = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.name} on {self.date} [{self.token}]"


class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)  
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms = models.TextField()  # comma-separated
    medicines = models.TextField()  # comma-separated
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField(default=False)

    @property
    def symptoms_list(self):
        return self.symptoms.split(',')

    @property
    def medicines_list(self):
        return self.medicines.split(',')
class Bed(models.Model):
    BED_STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Taken', 'Taken'),
        ('Occupied', 'Occupied'),
    ]
    id = models.AutoField(primary_key=True)  
    bed_no = models.PositiveIntegerField(unique=True)  # Unique bed number
    ventilator = models.BooleanField(default=False)  # Whether the bed has a ventilator
    status = models.CharField(
        max_length=10, choices=BED_STATUS_CHOICES, default='Available'
    )  # Occupancy status
    diagnosis = models.TextField(blank=True, null=True)  # Diagnosis of the patient occupying the bed
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of bed creation

    def __str__(self):
        return f"Bed {self.bed_no} ({self.status})"


# Patient Model



class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default='O+')  # Default value set here
    diagnosis = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, default='0000000000')
    admission_date = models.DateTimeField(default=timezone.now)
    discharge_date = models.DateTimeField(null=True , blank= True ,default=timezone.now)

    def __str__(self):
        return self.name

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
    ]
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)

    def __str__(self):
        return self.name