from email.policy import default
from django.forms import Form, IntegerField,CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm 
from django.forms import PasswordInput 
from django.contrib.auth.models import User 
from django import forms

from datetime import datetime

class EmployeeUserCustomCreationForm(UserCreationForm):
    email=EmailField()
    password1=CharField(label="Password",widget=PasswordInput)
    password2=CharField(label="Confirm Paasword",widget=PasswordInput)
    is_staff = 0
 
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        help_texts={"username":"","email":"", "password1":"", "password2":""}

class IT_TeamUserCustomCreationForm(UserCreationForm):
    email=EmailField()
    password1=CharField(label="Password",widget=PasswordInput)
    password2=CharField(label="Confirm Password",widget=PasswordInput)
#    is_staff = True
 
    class Meta:
        model=User
        #User.is_staff=True
        fields=["username","email","password1","password2"]
        help_texts={"username":"","email":"", "password1":"", "password2":""}

TICKET_CATEGORIES=(
    ("Request Generic Support","Request Generic Support"),
    ("Access Assistance","Access Assistance"),
    ("Business Applications","Business Applications"),
    ("Hardware Request","Hardware Request")
)

TICKET_STATUS=(
    ("Open","Open"),
    ("In Progress","In Progress"),
    ("Complete","Complete")
)

class Create_Ticket(Form):
    date_open = DateField(initial= datetime.now, label="Date Open")
    category = forms.CharField(label="Category",widget=forms.Select(choices=TICKET_CATEGORIES))
    description = CharField(max_length=500,label="Description")
    status = CharField(initial="Open") 

class Update_Ticket(Form):
    status = forms.CharField(label="Status",widget=forms.Select(choices=TICKET_STATUS))
