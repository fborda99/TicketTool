from django.urls import path
from AppTickets.views import *

urlpatterns = [
    path("index/",index, name="index"),
    path("",homepage,name="homepage"),
    path("login/",login_user, name= "login"),
    path("register/employee", register_employee, name = "register_employee"),
    path("register/it", register_it, name = "register_it"),
    path("tickets/",ticket)
]