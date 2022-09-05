from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from AppMessages.forms import *
from AppMessages.models import *
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

def messages(request):
    return render(request, "AppMessages/messages.html")

@login_required
def it_message_create(request):
    if request.method == "GET":
        new_message = MessageCreateForm(initial={"send_by":request.user.username})
        return render(request, "AppMessages/it_messages_create.html", {"message": new_message})
    else:
        new_message = MessageCreateForm(request.POST)
        
        if new_message.is_valid():
            data = new_message.cleaned_data
            message = data.get("message")
            send_by = data.get("send_by")
            date_send = data.get("date_send")
            ticket_number = data.get("ticket_number")

            new_message = Message(message=message,send_by=send_by,date_send=date_send,ticket_number=ticket_number)
            new_message.save()
            return redirect("it_message_list")

        else:
            return render(request, "AppMessages/it_form_error.html")

class ITMessageListView(ListView):
    model=Message
    template_name = "AppMessages/it_messages_list.html"

def it_messages_search(request):
    return render(request,"AppMessages/it_messages_search.html")

def it_message_results(request):
    ticket_number_search=request.GET.get("ticket_number", None)
 
    if not ticket_number_search:
        return render(request, "AppMessages/it_form_error.html")

    messages_list=Message.objects.filter(ticket_number=ticket_number_search)
    return render(request,"AppMessages/it_messages_results.html",{"messages":messages_list})

def employee_message_create(request):
    if request.method == "GET":
        new_message = MessageCreateForm(initial={"send_by":request.user.username})
        return render(request, "AppMessages/employee_messages_create.html", {"message": new_message})
    else:
        new_message = MessageCreateForm(request.POST)
        
        if new_message.is_valid():
            data = new_message.cleaned_data
            message = data.get("message")
            send_by = data.get("send_by")
            date_send = data.get("date_send")
            ticket_number = data.get("ticket_number")

            new_message = Message(message=message,send_by=send_by,date_send=date_send,ticket_number=ticket_number)
            new_message.save()
            return redirect("employee_message_list")

        else:
            return render(request, "AppMessages/employee_form_error.html")

class EmployeeMessageListView(ListView):
    model=Message
    template_name = "AppMessages/employee_messages_list.html"

def employee_messages_search(request):
    return render(request,"AppMessages/employee_messages_search.html")

def employee_message_results(request):
    ticket_number_search=request.GET.get("ticket_number", None)
 
    if not ticket_number_search:
        return render(request, "AppMessages/employee_form_error.html")

    messages_list=Message.objects.filter(ticket_number=ticket_number_search)
    return render(request,"AppMessages/employee_messages_result.html",{"messages":messages_list})
