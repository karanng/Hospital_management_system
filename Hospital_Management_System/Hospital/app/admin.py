from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Payment)

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'password')
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

