from django.urls import path
from AppMessages.views import *

urlpatterns = [
    path("messages/",messages)
]