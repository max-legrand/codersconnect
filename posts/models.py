from django.db import models
from users import models as usermodels
from datetime import date

# Create your models here.
class Postings(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.TextField(default="Remote")
    techstack = models.TextField(default="N/A")
    organization = models.ForeignKey(usermodels.Organization, default=None, on_delete=models.CASCADE)
    timestamp = models.DateField(default=date.today)
    status = models.BooleanField(default=True) # T == active F == closed
    applicants = models.IntegerField(default=0)
    image= models.TextField(default="http://via.placeholder.com/150")


class Connection(models.Model):
    post = models.ForeignKey(Postings, default=None, on_delete=models.CASCADE)
    accept_user = models.ForeignKey(usermodels.ExtendedUser, default=None, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    accepted = models.BooleanField(default=False)
