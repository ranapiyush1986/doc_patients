from django.contrib import admin
from patients import models
# from django.contrib.auth.models import Group


# admin.site.unregister(Group)
admin.site.register(models.Patients)
# admin.site.register(models.Appointments)
