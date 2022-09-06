from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppEmployees.forms import *
from AppEmployees.models import *
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from AppIT_Team.models import Avatar

#User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def employees(request):
    return render(request, "AppEmployees/employees.html")

@login_required
def employees_list(request):
    employess=Employee.objects.all()
    context={"employees":employess}
    return render(request, "appEmployees/Employees_list.html", context)

@login_required
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
    success_url = "/AppEmployees/employees/list"

@login_required
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
                employee=Employee.objects.get(id=id_employee)
                employee.name=data.get("name")
                employee.lastname=data.get("lastname")
                employee.email=data.get("email")
                employee.jobtitle=data.get("jobtitle")
                employee.workid=data.get("workid")
                employee.save()   
            except:
                return render(request,"AppMessages\employee_form_error.html")
        return redirect("employee_list")

class EmployeeDeatailView(DetailView):
    model=Employee
    template_name = "AppEmployees/employees_detailview.html"

@login_required
def employee_homepage(request):
    return render(request, "AppEmployees/employees_homepage.html")

@login_required
def employee_profile_user(request):
    try:
        avatar = Avatar.objects.filter(user = request.user).first()
        avatar_context = {"avatar":avatar.image.url}
        return render(request,"AppEmployees/employee_user_profile.html",avatar_context)
    except:
        return render(request,"AppEmployees/employee_user_profile.html")

@login_required
def employee_edit_user_email(request):
    if request=="GET":
        form=EmployeeUserEditEmailForm(initial={"email":request.user.email})
        return render(request,"AppEmployees/employee_user_update_email.html",{"form":form})
    
    else:
        form=EmployeeUserEditEmailForm(request.POST)
    
        if form.is_valid():
            data=form.cleaned_data
            user_it=request.user
            user_it.email=data["email"]
            user_it.save()
            return redirect("employee_profile_user")
        
        else:
            return render(request,"AppEmployees/employee_user_update_email.html",{"form":form})

@login_required
def employee_edit_user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            return redirect('employee_user_password_confirm')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'AppEmployees/employee_user_update_password.html', {'form': form })

@login_required
def employee_user_password_confirm(request):
    return render(request,"AppEmployees/employee_user_password_confirm.html")

@login_required
def employee_add_avatar(request):
    if request.method == "GET":
        form=EmployeeAvatarForm()
        context={"form":form}
        return render(request,"AppEmployees/employee_user_add_avatar.html",context)
 
    else:
        form=EmployeeAvatarForm(request.POST,request.FILES)
 
        if form.is_valid():
            data=form.cleaned_data
            user=User.objects.filter(username=request.user.username).first()
            avatar=Avatar(user=user,image=data["image"])
            avatar.save()
            return render(request,"AppEmployees/employees_homepage.html")

