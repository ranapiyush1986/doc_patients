from django.db import models
from django.contrib.auth import get_user_model
from patients.models import Patients


class Doctors(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='doctors_user')
   # specialised = models.CharField(max_length=15, default='PATIENT')
    specialised = models.ForeignKey('Specilaizations', on_delete=models.PROTECT,null=True,related_name='doctor_specialised')
    addr = models.CharField(max_length=155, null=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Appointments(models.Model):

    patients = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='appointments_patients')
    doctors = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='appointments_doctors')
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(null=True, blank=True)
    is_accepted = models.BooleanField(default=None, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return str(self.doctors)

class Specilaizations(models.Model):
    specialization_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.specialization_name)

