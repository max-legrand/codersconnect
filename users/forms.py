from django import forms
from . import models
from django.contrib.auth.models import User


class CreateExtendedUser(forms.ModelForm):
    class Meta:
        model = models.ExtendedUser
        fields = ['email', 'firstname', 'lastname']


class CreateOrg(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = ['email', 'organization_name']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
