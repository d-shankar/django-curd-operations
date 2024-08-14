from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .model import Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticate_user, allowed_users
from rest_framework import IsAdminUser
# Create your views here.

@login_required
@allowed_users(allowed_roles=['admin'])
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_templates/employee_list.html", context)

@login_required   
@allowed_users(allowed_roles=['admin','customers'])
def employee_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_templates/employee_form.html", {'form': form})
        
    else:
        if id ==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the employee list after saving
        else:
            return render(request, "employee_templates/employee_form.html", {'form': form})
            

@login_required
def employee_delete(request, id=0):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect("/employee/list")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'employee_templates/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'employee_templates/home.html')
