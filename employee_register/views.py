from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .model import Employee
# Create your views here.

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_templates/employee_list.html", context)
    
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
            


def employee_delete(request, id=0):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect("/employee/list")
