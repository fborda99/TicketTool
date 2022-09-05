from django.forms import Form, IntegerField,CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from datetime import datetime

class MessageCreateForm(Form):
    message=CharField(max_length=500,label="Message")
    send_by=CharField()
    date_send=DateField(initial=datetime.now,label="Date")
    ticket_number=IntegerField()

