import datetime

from django.utils import timezone

from django.db import models

from django.urls import reverse

from django.contrib.auth import get_user_model
class TaskManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(created_by=user)

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True)
    pub_date = models.DateTimeField('date published')
    due_date = models.DateTimeField('due date')
    created_by = models.ForeignKey(get_user_model(), null=False, related_name='tasks', on_delete=models.CASCADE)
    objects = TaskManager()

    def __unicode__(self):
        return self.name

    def is_published(self):
        return timezone.now() >= self.pub_date

    def get_absolute_url(self):
        return reverse('tasks:index')

