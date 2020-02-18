from django.db import models
from users import models as usermodels


# Create your models here.
class Postings(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    organization = models.ForeignKey(usermodels.Organization, default=None, on_delete="CASCADE")


class Connection(models.Model):
    post = models.ForeignKey(Postings, default=None, on_delete="CASCADE")
    accept_user = models.ForeignKey(usermodels.ExtendedUser, default=None, on_delete="CASCADE")
