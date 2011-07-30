import time
import hashlib

from django.db import models
from django.contrib.auth.models import User

def generate_key():
    return hashlib.sha224(str(time.time())).hexdigest()[:6]

# Create your models here.
class Manager(models.Model):
    user = models.OneToOneField(User)

class Developer(models.Model):
    user = models.OneToOneField(User)
    manager = models.ForeignKey(Manager)

class Invite(models.Model):
    manager = models.ForeignKey(Manager)
    key = models.CharField(max_length=6, default=generate_key)
    email = models.EmailField(unique=True)
    
from accounts import signals
    
