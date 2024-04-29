from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect
from app.models import Doctor
from app.models import Patient
from app.models import Appointment
from app.models import Payment
from django.db.models import Sum
def BASE(request):
    user = request.user
    return render(request, 'base.html',{'user': user})


def ADD_PATIENT(request):
    if request.method == "POST":
        patient_name = request.POST.get('patient_name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')


        patient = Patient(
            patient_Name = patient_name,
            date_of_birth = dob,
            age = age,
            phone = phone,
            gender = gender,
            email = email,
            address = address,
        )
        patient.save()
        print(patient_name,dob,age,phone,email,gender,address)
    return render(request,'patients/add_patient.html')


def PATIENTS(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patients.html',{'patients': patients})


def ADD_DOCTOR(request):
    if request.method == "POST":
        doctor_name = request.POST.get('Doctor_name')
        dob = request.POST.get('dob')
        specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        doctor_details = request.POST.get('doctor_details')
        address = request.POST.get('address')


        doctor = Doctor(
            doctor_name = doctor_name,
            date_of_birth = dob,
            specialization = specialization,
            experience = experience,
            age = age,
            phone = phone,
            gender = gender,
            email = email,
            doctor_details = doctor_details,
            address = address,
        )
        doctor.save()
        print(doctor_name,dob,specialization,experience,age,phone,gender,email,doctor_details,address)
    return render(request, 'doctors/add_doctor.html')


def DOCTORS(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctors.html',{'doctors': doctors})


def INDEX(request):
    patient_count = Patient.objects.count()
    doctors = Doctor.objects.all()
    appointment_count = Appointment.objects.count()
    appointments = Appointment.objects.all()
    payment_count = Payment.objects.count()
    total_revenue = Payment.objects.aggregate(total_revenue=Sum('treatment_cost'))['total_revenue'] or 0
    return render(request, 'index.html',{'patient_count': patient_count,'doctors': doctors,'appointment_count': appointment_count,'appointments': appointments,'payment_count': payment_count,'total_revenue': total_revenue})


def ADD_APPOINTMENT(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        department = request.POST.get('department')
        doctor_name = request.POST.get('doctor_name')
        appointment_date = request.POST.get('appointment_date')
        time_slot = request.POST.get('time_slot')
        token_number = request.POST.get('token_number')
        problem = request.POST.get('problem')

        appointment = Appointment(
            patient_id=patient_id,
            department=department,
            doctor_name=doctor_name,
            appointment_date=appointment_date,
            time_slot=time_slot,
            token_number=token_number,
            problem=problem,
        )
        appointment.save()
    return render(request, 'appointments/add_appointment.html')


def APPOINTMENTS(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointments.html',{'appointments': appointments})


def BLANK(request):
    return render(request, 'blank.html')




def signup(request):


    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sign up successful!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirect to a success page.
                return redirect('index')  # Change 'home' to your desired URL
            else:
                # Return an 'invalid login' error message.
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('base')


def ABOUT(request):
    return render(request, 'about.html')


def ADD_PAYMENT(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        patient_name = request.POST.get('patient_name')
        department = request.POST.get('department')
        doctor_name = request.POST.get('doctor_name')
        admission_date = request.POST.get('admission_date')
        discharge_date = request.POST.get('discharge_date')
        service_name = request.POST.get('service_name')
        treatment_cost = request.POST.get('treatment_cost')
        discount = request.POST.get('discount')
        advance_paid = request.POST.get('advance_paid')
        payment_type = request.POST.get('payment_type')
        card_check_no = request.POST.get('card_check')

        payment = Payment(
            patient_id=patient_id,
            patient_name=patient_name,
            department=department,
            doctor_name=doctor_name,
            admission_date=admission_date,
            discharge_date=discharge_date,
            service_name=service_name,
            treatment_cost=treatment_cost,
            discount=discount,
            advance_paid=advance_paid,
            payment_type=payment_type,
            card_check_no=card_check_no,
        )
        payment.save()
        return render(request, 'payments/add_payment.html', {'success_message': 'Payment added successfully.'})
    else:
        return render(request, 'payments/add_payment.html')


def PAYMENTS(request):
    payments = Payment.objects.all()
    return render(request, 'payments/payments.html', {'payments': payments})