from django import forms
from . import models
from django.contrib.auth.models import User


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Postings
        fields = ['title', 'description', 'location', 'techstack']
        