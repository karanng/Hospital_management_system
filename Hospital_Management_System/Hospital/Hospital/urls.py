from django.contrib import admin
from django.urls import path
from . import views
from .views import signup, user_login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BASE, name='base'),
    path('blank.html',views.BLANK,name='blank'),
    path('add-patient.html',views.ADD_PATIENT,name='add_patient'),
    path('patients.html',views.PATIENTS,name='all_patients'),
    path('add-doctor.html',views.ADD_DOCTOR,name='add_doctor'),
    path('doctors.html',views.DOCTORS,name='all_doctors'),
    path('index.html',views.INDEX,name='index'),
    path('add-appointment.html',views.ADD_APPOINTMENT,name='add_appointment'),
    path('appointments.html',views.APPOINTMENTS,name='all_appointments'),
    path('sign-up.html',signup,name='signup'),
    path('login.html',user_login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('about.html',views.ABOUT,name='about'),
    path('add-payment.html',views.ADD_PAYMENT,name='add_payment'),
    path('payments.html',views.PAYMENTS,name='all_payments'),

]
