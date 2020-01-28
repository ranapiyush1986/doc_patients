from django.forms import ModelForm
from patients import models


class PatientsProfileForm(ModelForm):
	class Meta:
		model = models.Patients
		# fields = '__all__'
		exclude = ('user', )
