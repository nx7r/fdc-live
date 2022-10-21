from distutils.text_file import TextFile
from django.db import models



class Participent(models.Model):
    full_name = models.CharField(max_length=50)
    extra_data = models.TextField(null = True)

    def __str__(self):
        return self.full_name



class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    dead_line = models.DateField(auto_now=False, auto_now_add=False)
    participents = models.ManyToManyField(Participent)

    def __str__(self):
        return self.name
