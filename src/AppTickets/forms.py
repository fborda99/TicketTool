from django.forms import Form, IntegerField,CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm 
from django.forms import PasswordInput 
from django.contrib.auth.models import User 

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
    password2=CharField(label="Confirm Paasword",widget=PasswordInput)
    is_staff = 1
 
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        help_texts={"username":"","email":"", "password1":"", "password2":""}