from django.urls import path
from AppTickets.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("index/",index, name="index"),
    path("",homepage,name="homepage"),
    path("login/",login_user, name= "login"),
    path("register/employee", register_employee, name = "register_employee"),
    path("register/it", register_it, name = "register_it"),
    path("tickets/",ticket),
    path("logout/",LogoutView.as_view(template_name="AppTickets/logout.html"),name="logout"),

#Tickets - Employees
    path("Ticket/create/",create_ticket_employee,name="create_ticket_employees"),
    path("Ticket/detail/<pk>",TicketDetailEmployee.as_view(),name="ticket_detail_employees"),
    path("Ticket/list/",TicketListEmployee.as_view(),name="ticket_list_employees"),
    path("Ticket/update/<id_ticket>",update_ticket_employee,name="update_ticket_employees"),
    
#Tickets - IT Team
    path("Ticket/it/detail/<pk>",TicketDetailIT.as_view(),name="ticket_detail_it"),
    path("Ticket/it/list/",TicketListIT.as_view(),name="ticket_list_it"),
    path("Ticket/it/update/<id_ticket>",update_ticket_it,name="update_ticket_it"),
]