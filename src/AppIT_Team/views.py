from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView 
from AppIT_Team.models import *
from AppIT_Team.forms import *
from django.http import HttpResponse

class IT_TeamList(ListView): 
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

def IT_TeamUpdate(request,id_IT_Member):
    if request.method=="GET":
        update_form=Update_Member()
        context={"update_form":update_form}
        return render(request,"AppIT_Team\it_member_form.html",context)
    else:
        update_form=Update_Member(request.POST)
        if update_form.is_valid():
            data=update_form.cleaned_data
            try:
                it_member=IT_Member.objects.get(id=id_IT_Member)
                it_member.name=data.get("name")
                it_member.lastname=data.get("lastname")
                it_member.email=data.get("email")
                it_member.jobtitle=data.get("jobtitle")
                it_member.save()
            except:
                return HttpResponse("Update error")
        return redirect("IT_Team_List")

def it_team_homepage(request):
    return render(request, "AppIT_Team/it_team_homepage.html")