from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_Name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=50)
    address = models.TextField()





    def __str__(self):
        return self.patient_Name

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=50)
    doctor_details = models.TextField()
    address = models.TextField()


    def __str__(self):
        return self.doctor_name
class Appointment(models.Model):
    patient_id = models.IntegerField()
    department = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    time_slot = models.CharField(max_length=100)
    token_number = models.IntegerField()
    problem = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient_id} with {self.doctor_name} on {self.appointment_date}"
class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
from django.db import models

class Payment(models.Model):
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    admission_date = models.DateField()
    discharge_date = models.DateField()
    service_name = models.CharField(max_length=100)
    treatment_cost = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    advance_paid = models.IntegerField()
    payment_type = models.CharField(max_length=50)
    card_check_no = models.IntegerField()

    def __str__(self):
        return f"Payment for {self.patient_name} ({self.patient_id})"
