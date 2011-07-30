from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manager(models.Model):
    user = models.OneToOneField(User)

class Developer(models.Model):
    user = models.OneToOneField(User)
    manager = models.ForeignKey(Manager)
    
