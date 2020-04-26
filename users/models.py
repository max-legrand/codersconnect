from django.db import models
from django.contrib.auth.models import User


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    firstname = models.CharField(max_length=50, verbose_name="First Name:")
    lastname = models.CharField(max_length=50, verbose_name="Last Name:")
    description = models.TextField(default="This user has not provided an about me.")
    image = models.TextField(default="http://via.placeholder.com/150")


class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    organization_name = models.CharField(max_length=55, verbose_name="Organization name:")
    description = models.TextField(default="This organization has not provided a description.")
    image = models.TextField(default="http://via.placeholder.com/150")
    #organization_blurb = models.TextFeild(max_length=200)
