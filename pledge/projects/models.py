from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from accounts import Manager, Developer

# Create your models here.
class Project(models.Model):
    manager = models.ForeignKey(Manager)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return selt.title
    
TASK_STATUS_CHOICES = (
    (1, 'Set task'),
    (2, 'Done task'),
    (3, 'Reset task'),
    (4, 'Approve task'),
)
class Task(models.Model):
    project = models.ForeignKey(Project)
    developers = models.ManyToManeField(Developer, relatated_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    task_code = models.CharField(max_length=6, unique=True)
    status = models.IntegerField(choices=TASK_STATUS_CHOICES, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title

class Commit(models.Model):
    task = models.ForeignKey(Task0
    text = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s %s' % (str(self.created_date), self.text)
    

class FileStorage(models.Model):
    filename = models.FielField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    description = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.description
