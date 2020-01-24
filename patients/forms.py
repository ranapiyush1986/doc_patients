from django.forms import ModelForm
from patients import models


class PatientsProfileForm(ModelForm):
	class Meta:
		model = models.Patients
		# fields = '__all__'
		exclude = ('user', )

	# def save(self, commit=True):
	# 	user = super(PatientsProfileForm, self).save(commit=False)
	# 	user.user = self.request.user
	#
	# 	if commit:
	# 		user.save()
	# 	return user