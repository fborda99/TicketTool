from django.shortcuts import render, redirect
from django.http import HttpResponse

#form creation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppEmployees.forms import *
from AppEmployees.models import *

from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView



def employees(request):
    return render(request, "AppEmployees/employees.html")

def employees(request):
    employess=Employee.objects.all()
    context={"employees":employess}
    return render(request, "appEmployees/Employees_list.html", context)

def EmployeeCreate(request):
    if request.method == "GET":
        employee = EmployeeCreateForm
        return render(request, "AppEmployees/employee_create.html", {"employee": employee})
    else:
        employee = EmployeeCreateForm(request.POST)
        
        if employee.is_valid():
            data = employee.cleaned_data
            name = data.get("name")
            lastname = data.get("lastname")
            email = data.get("email")
            job_title = data.get("job_title")
            workid=data.get("workid")

            new_employee = Employee(name=name,lastname=lastname,email=email,job_title=job_title, workid= workid)
            new_employee.save()
            return redirect("employee_list")

        else:
            return HttpResponse("The form for creating the employee is not valid. Please try again!")

class EmployeeDelete(DeleteView):
     model = Employee
     template_name = "AppEmployees/employee_confirm_delete.html"
     success_url = "/AppEmployees/employees/"

def EmployeeUpdate(request, id_employee):
    if request.method=="GET":
        update_form=EmployeeEditForm()
        context={"update_form":update_form}
        return render(request,"AppEmployees/employee_update.html",context)
        
    else:
        update_form=EmployeeEditForm(request.POST)
        if update_form.is_valid():
            data=update_form.cleaned_data
            try:
                employee=employees.objects.get(id=id_employee)
                employee.name=data.get("name")
                employee.lastname=data.get("lastname")
                employee.email=data.get("email")
                employee.jobtitle=data.get("jobtitle")
                employee.workid=data.get("workid")
                employee.save()   
            except:
                return HttpResponse("Update error")
        return redirect("employee_list")


class EmployeeDeatailView(DetailView):
    model=Employee
    template_name = "AppEmployees/employees_detailview.html"

def employee_homepage(request):
    return render(request, "AppEmployees/employees_homepage.html")