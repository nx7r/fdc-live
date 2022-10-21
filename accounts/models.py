from email.policy import default
from enum import unique
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null = True,)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True)
    major = models.CharField(max_length=50)
    address = models.TextField(max_length = 1000)
    acadimic_year = models.IntegerField(
        default=1,
     )
    univ_fac = models.CharField(max_length = 90,null=True)
    auth = 0

    DEPARTEMENT_CHOICES = [
        ('ME','Men...'),
        ('WI','WI...'),
    ]

    departement = models.CharField(
        max_length=2,
        choices=DEPARTEMENT_CHOICES,
        default='ME',
    )
    rate = models.IntegerField(
        default=0,
    )
    facebook_link = models.CharField(max_length=100, null = True)

    def __str__(self):
        return str(self.full_name)
    
    @receiver(post_save, sender= User)
    def create_member(sender, instance, created,**kwargs):
        if created:
            print('createmember')
            Member.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_member(sender, instance, **kwargs):
        print()
        print('here')
        #instance.member.save()