from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView 
from AppIT_Team.models import *
from AppIT_Team.forms import *
from django.http import HttpResponse

#User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User

class IT_TeamList(ListView): 
    model=IT_Member
    template_name="AppIT_Team/it_team_list.html"

class IT_TeamDetail(DetailView):
    model=IT_Member
    template_name="AppIT_Team/it_team_detail.html"

@login_required
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

@login_required
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

@login_required
def it_team_homepage(request):
    return render(request, "AppIT_Team/it_team_homepage.html")

@login_required
def it_profile_user(request):
    try:
        avatar = Avatar.objects.filter(user = request.user).first()
        avatar_context = {"avatar":avatar.image.url}
        return render(request,"AppIT_Team/it_user_profile.html",avatar_context)
    except:
        return render(request,"AppIT_Team/it_user_profile.html")

@login_required
def it_edit_user_email(request):
    if request=="GET":
        form=ITUserEditEmailForm()
        return render(request,"AppIT_Team/it_user_update_email.html",{"form":form})
    
    else:
        form=ITUserEditEmailForm(request.POST)
    
        if form.is_valid():
            data=form.cleaned_data
            user_it=request.user
            user_it.email=data["email"]
            user_it.save()
            return redirect("it_profile_user")
        
        else:
            return render(request,"AppIT_Team/it_user_update_email.html",{"form":form})

@login_required
def it_edit_user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            return redirect('it_user_password_confirm')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'AppIT_Team/it_user_update_password.html', {'form': form })

@login_required
def it_user_password_confirm(request):
    return render(request,"AppIT_Team/it_user_password_confirm.html")

@login_required
def it_add_avatar(request):
    if request.method == "GET":
        form=ITAvatarForm()
        context={"form":form}
        return render(request,"AppIT_Team/it_user_add_avatar.html",context)
 
    else:
        form=ITAvatarForm(request.POST,request.FILES)
 
        if form.is_valid():
            data=form.cleaned_data
            user=User.objects.filter(username=request.user.username).first()
            avatar=Avatar(user=user,image=data["image"])
            avatar.save()
            return render(request,"AppIT_Team/it_team_homepage.html")

