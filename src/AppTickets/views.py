from django.shortcuts import render, redirect
from django.http import HttpResponse


#Login
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login


#Register Form
from AppTickets.forms import *



def homepage(request):
    return render(request,"AppTickets/homepage.html" )

def index(request):
    return render(request, "AppTickets/index.html")

def ticket(request):
    return render(request, "AppTickets/tickets.html")


def login_user(request):
    if request.method == "GET":
        form=AuthenticationForm()
        context={"form":form}
        return render(request,"AppTickets/login.html",context)
        
    else:
        form = AuthenticationForm(request,data=request.POST)
 
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(username=data.get("username"),password=data.get("password"))
 
            if user is not None:
                auth_login(request,user)
                if user.is_staff == 1:
                    return redirect("IT_Team_List")
                else:
                    return redirect("employee_list")
        
            else:
                context={
                    "error":"Please enter valid credentials",
                    "form": form
                }
                return (request,"AppTickets/login.html",context)
            
        else:
            context={
            "error":"Please enter valid credentials",
            "form": form
            }
            return render(request,"AppTickets/login.html",context)



def register_employee(request):
    if request.method == "GET":
        form=EmployeeUserCustomCreationForm()
        return render(request,"AppTickets/register_employee.html",{"form":form})
        
    else:
        form=EmployeeUserCustomCreationForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    
    else:
        return render(request,"AppTickets/register_employee.html",{"form":form,"error":"Form not valid."})


def register_it(request):
    if request.method == "GET":
        form=IT_TeamUserCustomCreationForm()
        return render(request,"AppTickets/register_it_team.html",{"form":form})
        
    else:
        form=IT_TeamUserCustomCreationForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect("IT_Team_List")
    
    else:
        return render(request,"AppTickets/register_it_team.html",{"form":form,"error":"Form not valid."})