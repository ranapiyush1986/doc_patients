from django.contrib import admin
from doctors import models
# from django.contrib.auth.models import Group


# admin.site.unregister(Group)
admin.site.register(models.Doctors)
admin.site.register(models.Appointments)
