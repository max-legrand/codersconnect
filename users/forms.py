from django import forms
from . import models


class CreateExtendedUser(forms.ModelForm):
    class Meta:
        model = models.ExtendedUser
        fields = ['email', 'firstname', 'lastname']


class CreateOrg(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = ['email', 'organization_name']
