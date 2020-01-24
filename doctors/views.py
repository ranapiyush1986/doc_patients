from django.http import HttpResponseRedirect
from django.shortcuts import render
from doctors import models
from doctors import forms


def doctors(request):
    doctors_list = models.Doctors.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors_list})


def appointments_create(request, id):

    if request.method == 'POST':
       

        form = forms.AppointmentsForm(request.POST)
        if form.is_valid():
            form.set_doctor(models.Doctors.objects.get(pk=id).user)
            form.set_patients(request.user)
            form.save()
    else:
        form = forms.AppointmentsForm()

    return render(request, 'appointments_create.html', {'form': form})


def appointments_accept(request, id):

    appointments = models.Appointments.objects.get(pk=id)

    if request.GET['accept'] == 'true':
        appointments.is_accepted = True
    else:
        appointments.is_accepted = False

    appointments.save()

    return HttpResponseRedirect('/doctors/appointments/')


def appointments(request):
    appointments_list = models.Appointments.objects.filter(doctors=request.user)
    return render(request, 'appointments.html', {'appointments': appointments_list})
