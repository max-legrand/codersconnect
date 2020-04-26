from django import forms
from . import models
from django.contrib.auth.models import User


class CreateExtendedUser(forms.ModelForm):
    class Meta:
        model = models.ExtendedUser
        fields = ['email', 'firstname', 'lastname', 'description', 'image']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': "form-control"}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'})
        }


class CreateOrg(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = ['email', 'organization_name', 'description', 'image']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'organization_name': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
