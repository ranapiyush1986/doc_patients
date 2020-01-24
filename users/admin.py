from django.contrib import admin
from users import models
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.register(models.User)
