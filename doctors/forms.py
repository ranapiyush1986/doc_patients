from django.forms import ModelForm
from doctors import models

class SpecializationForm(ModelForm):
	class Meta:
		model=models.Specilaizations
		fields = '__all__'

class DoctorsProfileForm(ModelForm):
	class Meta:
		model = models.Doctors
		# fields = '__all__'
		exclude = ('user', )

	# def save(self, commit=True):
	# 	user = super(DoctorsProfileForm, self).save(commit=False)
	# 	# user.user = self.request.user
	#
	# 	if commit:
	# 		user.save()
	# 	return user


class AppointmentsForm(ModelForm):
	class Meta:
		model = models.Appointments
		# fields = '__all__'
		exclude = ('patients', 'is_accepted', 'doctors', )

	def set_patients(self, data):
		self.instance.patients = data

	def set_doctor(self, data):
		self.instance.doctors = data

	def save(self, commit=True):
		user = super(AppointmentsForm, self).save(commit=False)
		# user.patients = self.request.user

		if commit:
			user.save()
		return user
