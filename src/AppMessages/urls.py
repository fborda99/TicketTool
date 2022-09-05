from django.urls import path
from AppMessages.views import *

urlpatterns = [
    #IT
    path("messages/it/new/",it_message_create,name="it_message_create"),
    path("messages/it/list/",ITMessageListView.as_view(),name="it_message_list"),
    path("messages/it/search/",it_messages_search,name="it_message_search"),
    path("messages/it/results/",it_message_results,name="it_message_results"),

    #Employees
    path("messages/employee/new/",employee_message_create,name="employee_message_create"),
    path("messages/employee/list/",EmployeeMessageListView.as_view(),name="employee_message_list"),
    path("messages/employee/search/",employee_messages_search,name="employee_message_search"),
    path("messages/employee/results/",employee_message_results,name="employee_message_results"),
]