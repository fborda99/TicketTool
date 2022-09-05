from django.forms import Form, IntegerField,CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from datetime import datetime

class MessageCreateForm(Form):
    message=CharField(max_length=500,label="Message")
    send_by=CharField()#initial=request.user)
    date_send=DateField(initial=datetime.now,label="Date")

