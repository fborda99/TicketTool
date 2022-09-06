from django.forms import Form, IntegerField,CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from django import forms

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

class EmployeeCreateForm(Form):
    name=CharField(max_length=50,label="First Name")
    lastname=CharField(max_length=50,label="Last Name")
    email=EmailField(label="Email")
    job_title= CharField(label="Job Title",widget=forms.Select(choices=JOB_TITLE_CHOICES))
    workid = CharField(label="Work ID")

class EmployeeEditForm(Form):
    name=CharField(label="Name")
    lastname=CharField(label = "Last Name")
    email=EmailField(label = "Email")
    job_title=CharField(label = "Job Title",widget=forms.Select(choices=JOB_TITLE_CHOICES))
    workid=CharField(label = "Work ID") 

class EmployeeUserEditEmailForm(Form):
    email=EmailField(label="New Email")
 
    class Meta:
        model=User
        fields=["email"]
        help_texts={"email":""}

class EmployeeAvatarForm(Form):
    image=ImageField()
 