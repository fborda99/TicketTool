from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView 
from AppIT_Team.models import *
from AppIT_Team.forms import *
from django.http import HttpResponse

class IT_TeamList(ListView): #THIS IS THE INDEX OF THE APPIT_TEAM
    model=IT_Member
    template_name="AppIT_Team/it_team_list.html"

class IT_TeamDetail(DetailView):
    model=IT_Member
    template_name="AppIT_Team/it_team_detail.html"

def IT_TeamCreate(request):
    if request.method == "GET":
        member = Create_Member
        return render(request, "AppIT_Team/it_team_create.html", {"member": member})

    else:
        member = Create_Member(request.POST)
        
        if member.is_valid():
            data = member.cleaned_data
            name = data.get("name")
            lastname = data.get("lastname")
            email = data.get("email")
            jobtitle = data.get("jobtitle")

            new_member = IT_Member(name=name,lastname=lastname,email=email,jobtitle=jobtitle)
            new_member.save()
            return redirect("IT_Team_List")

        else:
            return HttpResponse("The form for creating the new member is not valid. Please try again!")
    
class IT_TeamDelete(DeleteView):
    model=IT_Member
    template_name = "AppIT_team/it_member_confirm_delete.html"
    success_url="/AppIT_Team/list/"

class IT_TeamUpdate(UpdateView):
    model=IT_Member
    success_url="/AppIT_Team/list/"
    fields=["name","lastname","email","jobtitle"]

