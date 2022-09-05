from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView 
from AppTickets.models import *

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

def login_user_employee(request):
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
                if user.is_staff == 0:
                    return redirect("employee_list")
                else:
                    context={
                        "error":"You are not registered as an Employee. Please try again.",
                        "form": form
                    }
                    return render(request,"AppTickets/login.html",context)
        
            else:
                context={
                    "error":"Please enter valid credentials",
                    "form": form
                }
                return render(request,"AppTickets/login.html",context)
            
        else:
            context={
            "error":"Please enter valid credentials",
            "form": form
            }
            return render(request,"AppTickets/login.html",context)

def login_user_it(request):
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
                    context={
                    "error":"You are not registered as an IT Memeber. Please try again.",
                    "form": form
                    }
                    return render(request,"AppTickets/login.html",context)
        
            else:
                context={
                    "error":"Please enter valid credentials.",
                    "form": form
                }
                return render(request,"AppTickets/login.html",context)
            
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
        return redirect("homepage")
    
    else:
        return render(request,"AppTickets/register_employee.html",{"form":form,"error":"Form not valid."})

def register_it(request):
    if request.method == "GET":
        form=IT_TeamUserCustomCreationForm()#(initial={User.is_staff: True})
        return render(request,"AppTickets/register_it_team.html",{"form":form})
        
    else:
        form=IT_TeamUserCustomCreationForm(request.POST)
    
    if form.is_valid():
     #   form.is_staff=True
      #  form.User.is_staff=True
        form.save()
        return redirect("homepage")
    
    else:
        return render(request,"AppTickets/register_it_team.html",{"form":form,"error":"Form not valid."})

def create_ticket_employee(request):
    if request.method == "GET":
        ticket = Create_Ticket
        return render(request, "AppTickets/employee_ticket_create.html", {"ticket": ticket})

    else:
        ticket = Create_Ticket(request.POST)
        
        if ticket.is_valid():
            data = ticket.cleaned_data
            date_open = data.get("date_open")
            category = data.get("category")
            description = data.get("description")
            status = data.get("status")

            new_ticket = Ticket(date_open=date_open,category=category,description=description,status=status)
            new_ticket.save()
            return redirect("ticket_list_employees") 

        else:
            return HttpResponse("The form for creating the new ticket is not valid. Please try again!")

class TicketDetailEmployee(DetailView):
    model=Ticket
    template_name="AppTickets/employee_ticket_detail.html"

class TicketListEmployee(ListView): 
    model=Ticket
    template_name="AppTickets/employee_ticket_list.html"

def update_ticket_employee(request,id_ticket):
    if request.method=="GET":
        update_form=Update_Ticket()
        context={"update_form":update_form}
        return render(request,"AppTickets/employee_ticket_form.html",context)
    else:
        update_form=Update_Ticket(request.POST)
        if update_form.is_valid():
            data=update_form.cleaned_data
            try:
                ticket = Ticket.objects.get(id=id_ticket)
                ticket.status = data.get("status")
                ticket.save()
            except:
                return HttpResponse("Update error")
        return redirect("ticket_list_employees")

class TicketListIT(ListView): 
    model=Ticket
    template_name="AppTickets/it_ticket_list.html"

class TicketDetailIT(DetailView):
    model=Ticket
    template_name="AppTickets/it_ticket_detail.html"

def update_ticket_it(request,id_ticket):
    if request.method=="GET":
        update_form=Update_Ticket(initial={"status":Ticket.status})
        context={"update_form":update_form}
        return render(request,"AppTickets/it_ticket_form.html",context)
    else:
        update_form=Update_Ticket(request.POST)
        if update_form.is_valid():
            data=update_form.cleaned_data
            try:
                ticket = Ticket.objects.get(id=id_ticket)
                ticket.status = data.get("status")
                ticket.save()
            except:
                return HttpResponse("Update error")
        return redirect("ticket_list_it")

