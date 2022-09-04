from django.urls import path
from AppEmployees.views import *



urlpatterns = [
    path("homepage/",employee_homepage, name="homepage_employee"),
    path("employees/create/",EmployeeCreate,name = 'employee_create'),
    path("update/<id_employee>", EmployeeUpdate, name= "employee_update"),
    path("delete/<pk>",EmployeeDelete.as_view(),name = 'employee_delete'),
    path("detail/<pk>",EmployeeDeatailView.as_view(),name="employee_details"),
    path("employees/list",employees, name ='employee_list'),

#User
    path("user/profile",employee_profile_user, name = "employee_profile_user"),
    path("user/edit/email",employee_edit_user_email, name = "employee_edit_user_email"),
    path("user/edit/password",employee_edit_user_password, name = "employee_edit_user_password"),
    path("user/edit/password/success",employee_user_password_confirm, name = "employee_user_password_confirm"),
    path("user/edit/avatar/",employee_add_avatar, name = "employee_add_avatar"),
]
