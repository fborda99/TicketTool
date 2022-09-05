from django.forms import Form, IntegerField, CharField, DateField, EmailField, PasswordInput, ImageField
from django import forms
from AppIT_Team.models import *

#User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

JOB_TITLE_CHOICES=(
    ("Associate","Associate"),
    ("Senior Associate","Senior Associate"),
    ("Manager","Manager"),
    ("Senior Manager","Senior Manager"),
    ("Partner","Partner"),
    ("Director","Director")
)

class Create_Member(Form):
    name=CharField(max_length=50,label="First Name")
    lastname=CharField(max_length=50,label="Last Name")
    email=EmailField()
    jobtitle= forms.CharField(label="Job Title",widget=forms.Select(choices=JOB_TITLE_CHOICES))

class Update_Member(Form):
    name=CharField(label="First Name")
    lastname=CharField(label="Last Name")
    email=EmailField()
    jobtitle= forms.CharField(label="Job Title",widget=forms.Select(choices=JOB_TITLE_CHOICES))

class ITUserEditEmailForm(Form):
    email=EmailField(label="New Email")
 
    class Meta:
        model=User
        fields=["email"]
        help_texts={"email":""}

class ITAvatarForm(Form):
    image=ImageField()
