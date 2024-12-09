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
    # Fetch the existing employee instance
    employee_obj = get_object_or_404(employee, id=id)
    person_obj = employee_obj.person

    if request.method == "POST":
        person_form = personform(request.POST, instance=person_obj)
        employee_form = employeeform(request.POST, instance=employee_obj)

        if person_form.is_valid() and employee_form.is_valid():
            person_form.save()
            employee_form.save(commit=False)  
            employee_form.instance.person = person_form.instance  
            employee_form.instance.save()  
            return redirect('employee') 
        else:
            print(person_form.errors)
            print(employee_form.errors)
    else:
        person_form = personform(instance=person_obj)
        employee_form = employeeform(instance=employee_obj)

    return render(request, 'employee-edit.html', {'employee': employee_obj, 'person_form': person_form, 'employee_form': employee_form})

def employee_view(request, id):
    employee_obj = get_object_or_404(employee, id=id)
    return render(request, 'employee-view.html', {'employee': employee_obj})

def role_list(request):
    all_roles = role.objects.all()  # Get all roles
    role_counts = {}

    for role_item in all_roles:  # Iterate over each role
        role_counts[role_item] = employee.objects.filter(role=role_item).count()

    # Pass the roles and counts to the template
    return render(request, 'role-list.html', {'roles_with_counts': role_counts, 'roles': all_roles})



def role_create(request):
    return render(request,'role-create.html')

def role_view(request, id):
    role_obj = get_object_or_404(role, id=id)
    return render(request,'role-view.html', {'role': role_obj})

def role_edit(request, id):
    role_obj = get_object_or_404(role, id=id)
    return render(request,'role-edit.html' , {'role': role_obj})