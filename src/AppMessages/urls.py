from django.urls import path
from AppMessages.views import *

urlpatterns = [
    path("messages/",messages),

    #IT
    path("messages/it/new/",it_message_create,name="it_message_create"),
    path("messages/it/list/",ITMessageListView.as_view(),name="it_message_list"),

    #Employees
]