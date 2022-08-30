from django.forms import Form, IntegerField, CharField, DateField, EmailField
from AppIT_Team.models import *

#class IT_MemberForm(ModelForm):
    #class Meta:
     #   model = IT_Member
      #  fields = ['job_title']

#JOB_TITLES=(
 #   ("Associate","Associate"),
  #  ("Senior Associate","Senior Associate"),
   # ("Manager","Manager"),
#    ("Senior Manager","Senior Manager"),
 #   ("Partner","Partner"),
  #  ("Director","Director")
#)

class Create_Member(Form):
    name=CharField(max_length=50)
    lastname=CharField(max_length=50)
    email=EmailField()
    jobtitle=CharField(max_length=50)#,choices=JOB_TITLES) #FALTA TERMINAR Y TESTEAR

class Update_Member(Form):
    name=CharField()
    lastname=CharField()
    email=EmailField()
    jobtitle=CharField()#,choices=JOB_TITLES) #FALTA TERMINAR Y TESTEAR