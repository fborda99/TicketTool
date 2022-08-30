from django.urls import path
from AppTickets.views import *

urlpatterns = [
    path("index/",index),
    path("tickets/",ticket)
]