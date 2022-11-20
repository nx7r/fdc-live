from distutils.text_file import TextFile
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from . import models

# Create your forms here.

class MemberForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]


class MemberChangeForm(forms.ModelForm):
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    major = forms.CharField(required=False)
    address = forms.Textarea()
    acadimic_year = forms.ChoiceField(choices=[(1,'L1'),(1,'L1'),(2,'L2'),(3,'L3'),(4,'M1'),(5,'M2')], required=False)
    univ_fac = forms.CharField(required=False)

    class Meta:
        model = models.Member
        fields = ('full_name','email','phone_number','major','address','acadimic_year','univ_fac')
