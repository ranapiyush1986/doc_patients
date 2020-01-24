from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users import forms
from django.contrib.auth import authenticate, login, logout
from doctors.forms import DoctorsProfileForm
from patients.forms import PatientsProfileForm
from doctors.models import Doctors
from patients.models import Patients
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


def home(request):
    return render(request, 'home.html')


def profile(request):

    if request.user.type == "DOCTOR":
        instance, created = Doctors.objects.get_or_create(user=request.user)

        if request.method == 'POST':

            form = DoctorsProfileForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
        else:
            form = DoctorsProfileForm(instance=instance)

        return render(request, 'profile.html', {'form': form})

    else:

        instance, created = Patients.objects.get_or_create(user=request.user)

        if request.method == 'POST':

            form = PatientsProfileForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
        else:
            form = PatientsProfileForm(instance=instance)

        return render(request, 'profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/user/login')


def signin(request):
    messages = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.type == 'PATIENT':
                return HttpResponseRedirect('/doctors/')
            elif user.type == 'DOCTOR':
                return HttpResponseRedirect('/doctors/appointments/')
        else:
            messages = 'check email or password'

    return render(request, 'login.html', {"messages": messages})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            # print(username, raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            if user.type == "DOCTOR":
                bar = Doctors.objects.create(user=user)
                bar.save()
            else:
                bar = Patients.objects.create(user=user)
                bar.save()
            return redirect('/user/profile/')
    else:
        form = forms.SignupForm()
    return render(request, 'signup.html', {'form': form})
