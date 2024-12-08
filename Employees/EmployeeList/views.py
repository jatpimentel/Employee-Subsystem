from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import person,role,employee,access_rights
from .forms import personform,employeeform

# Create your views here.
def index(request):
    return render (request,'index.html')

def employee_list(request):
    all_employees = employee.objects.all
    return render (request,'employee-list.html', {'employees':all_employees})

def employee_create(request):
    if request.method == "POST":
        person_form = personform(request.POST)
        employee_form = employeeform(request.POST)
        if person_form.is_valid() and employee_form.is_valid():
            person_instance = person_form.save()
            employee_instance = employee_form.save(commit=False)
            employee_instance.person = person_instance
            employee_instance.save()

            return redirect('employee') 
        else:
            print(person_form.errors)
            print(employee_form.errors)

    else:
        person_form = personform()  
        employee_form = employeeform()  

    return render(request, 'employee-create.html', {'person_form': person_form, 'employee_form': employee_form})


def employee_edit(request, id):
    employee_obj = get_object_or_404(employee, id=id)
    if request.method == "POST":
        person_form = personform(request.POST)
        employee_form = employeeform(request.POST)
        if person_form.is_valid() and employee_form.is_valid():
            person_instance = person_form.save()
            employee_instance = employee_form.save(commit=False)
            employee_instance.person = person_instance
            employee_instance.save()

            return redirect('employee') 
        else:
            print(person_form.errors)
            print(employee_form.errors)

    else:
        person_form = personform()  
        employee_form = employeeform()  
    # Pass the employee object to the template
    return render(request, 'employee-edit.html', {'employee': employee_obj,'person_form': person_form, 'employee_form': employee_form})




def employee_view(request, id):
    employee_obj = get_object_or_404(employee, id=id)
    return render(request, 'employee-view.html', {'employee': employee_obj})
