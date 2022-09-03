from django.db import models

# Models for AppTickets


class Ticket(models.Model):
    date_open=models.DateField(blank=True, null=True)
    status=models.CharField(max_length=50) #dropdown, cuando se crea el ticket el default debería ser open
    category=models.CharField(max_length=50) #dropdown
    description=models.CharField(max_length=500)