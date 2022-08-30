from django.urls import path
from AppEmployees.views import *

urlpatterns = [
    path("employees/",employees)
]