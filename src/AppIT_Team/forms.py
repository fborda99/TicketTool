from django.forms import Form, IntegerField, CharField, DateField, EmailField
from django import forms
from AppIT_Team.models import *

JOB_TITLE_CHOICES=(
    ("associate","Associate"),
    ("aenior associate","Senior Associate"),
    ("manager","Manager"),
    ("senior manager","Senior Manager"),
    ("partner","Partner"),
    ("director","Director")
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
