import time
import hashlib

from django.db import models
from django.contrib.auth.models import User

def generate_key():
    return hashlib.sha224(str(time.time())).hexdigest()[:6]

class Manager(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return unicode(self.user)

    def __unicode__(self):
        return self.user.get_full_name()


class Developer(models.Model):
    user = models.OneToOneField(User)
    manager = models.ForeignKey(Manager)
    
    def __unicode__(self):
        return unicode(self.user)

    def __unicode__(self):
        return self.user.get_full_name()


class Invite(models.Model):
    manager = models.ForeignKey(Manager)
    key = models.CharField(max_length=6, default=generate_key)
    email = models.EmailField(unique=True)
    is_used = models.BooleanField(default = False)
    
from accounts import signals
    
