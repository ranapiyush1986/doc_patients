from django.db import models
from django.contrib.auth import get_user_model


USER_GENDER = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'))


class Patients(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='patients_user')
    bloodgroup = models.CharField(max_length=10, blank=True, null=True)
    sex = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.user)
