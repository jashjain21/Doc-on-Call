from django.contrib import admin
from .models import Patient,Patient_Record,Appointment
# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Patient_Record)
