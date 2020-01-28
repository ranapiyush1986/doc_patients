
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.text import capfirst
from django.utils.translation import gettext, gettext_lazy as _
from users import models
# from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)

    class Meta:
        model = models.User
        # fields = '__all__'
        fields = ("first_name", "last_name", "email","mobile", "password2", "password1", "type")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.mobile = self.cleaned_data["mobile"]
        if commit:
            user.save()
        return user
