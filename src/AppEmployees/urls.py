from django.urls import path
from AppEmployees.views import *

urlpatterns = [
    path("employees/",employees, name="employee"),

    path("employees/create/",EmployeeCreate,name = 'employee_create'),
    path("update/<id_employee>", EmployeeUpdate, name= "employee_update"),
    path("delete/<pk>",EmployeeDelete.as_view(),name = 'employee_delete'),
    path("detail/<pk>",EmployeeDeatailView.as_view(),name="employee_details"),
    path("employees/list",employees, name ='employee_list')
    
    
]
