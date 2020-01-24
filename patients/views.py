from django.shortcuts import render
from patients import models
from doctors import forms
from doctors.models import Appointments


def appointments(request):
    doctors_list = Appointments.objects.filter(patients=request.user)
    return render(request, 'appointments_patients.html', {'appointments': doctors_list})
