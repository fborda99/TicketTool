from django.db import models

# Create your models here.

class Message(models.Model):
    message=models.CharField(max_length=500)
    send_by=models.CharField(max_length=500)
    date_send=models.DateField(blank=True, null=True)
    ticket_number=models.IntegerField(default=1)
