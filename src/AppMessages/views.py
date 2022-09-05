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

            new_message = Message(message=message,send_by=send_by,date_send=date_send)
            new_message.save()
            return redirect("it_message_list")

        else:
            return HttpResponse("The form for creating the employee is not valid. Please try again!")

class ITMessageListView(ListView):
    model=Message
    template_name = "AppMessages/it_messages_list.html"
