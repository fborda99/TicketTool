from django.shortcuts import render
from django.http import HttpResponse

def it_team(request):
    return render(request, "AppIT_Team/it_team.html")
