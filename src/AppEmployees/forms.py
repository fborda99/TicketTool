from django.forms import Form, IntegerField,CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from django import forms

#User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

JOB_TITLE_CHOICES=(
    ("",""),
    ("associate","Associate"),
    ("aenior associate","Senior Associate"),
    ("manager","Manager"),
    ("senior manager","Senior Manager"),
    ("partner","Partner"),
    ("director","Director")
)

class EmployeeCreateForm(Form):
    name=CharField(max_length=50,label="First Name")
    lastname=CharField(max_length=50,label="Last Name")
    email=EmailField()
    job_title= forms.CharField(label="Job Title",widget=forms.Select(choices=JOB_TITLE_CHOICES))
    workid = CharField(max_length=15, label="workid")

class EmployeeEditForm(Form):
    name=CharField(label="Name")
    lastname=CharField(label = "Last Name")
    job_title=CharField(label = "job Title",widget=forms.Select(choices=JOB_TITLE_CHOICES))
    email=EmailField(label = "email")
    workid=IntegerField(label = "workid") 

class EmployeeUserEditEmailForm(Form):
    email=EmailField(label="New Email")
 
    class Meta:
        model=User
        fields=["email"]
        help_texts={"email":""}

class EmployeeAvatarForm(Form):
    image=ImageField()
 