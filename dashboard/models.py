from django.db import models
from accounts.models import Member

# Create your models here.
class Notification(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    target = models.ManyToManyField(Member)

    def __str__(self):
        return self.name

class Task(models.Model):
    _title = models.CharField(max_length=50)
    desc = models.TextField()
    start = models.DateTimeField(auto_now=False, auto_now_add=False)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self._title

