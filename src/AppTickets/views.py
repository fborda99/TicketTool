from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "AppTickets/index.html")

def ticket(request):
    return render(request, "AppTickets/tickets.html")