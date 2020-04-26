from django.db import models
from django.contrib.auth.models import User


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    firstname = models.CharField(max_length=50, verbose_name="First Name:")
    lastname = models.CharField(max_length=50, verbose_name="Last Name:")


class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    organization_name = models.CharField(max_length=55, verbose_name="Organization name:")
    #organization_blurb = models.TextFeild(max_length=200)
