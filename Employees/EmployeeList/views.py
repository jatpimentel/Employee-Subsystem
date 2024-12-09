from django.shortcuts import render, get_object_or_404, redirect
from .models import person, employee
from .forms import personform, employeeform

# Create your views here.
def index(request):
    return render(request, 'index.html')

def employee_list(request):
    # Default to 'all' if no status is selected
    status_filter = request.GET.get('status', 'all')
    
    if status_filter == 'active':
        employees = employee.objects.filter(employee_status='active')
    elif status_filter == 'inactive':
        employees = employee.objects.filter(employee_status='inactive')
    else:  # Default to 'all'
        employees = employee.objects.all()

    context = {
        'employees': employees,
        'status_filter': status_filter,  # Pass status for debugging if needed
    }
    return render(request, 'employee-list.html', context)


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
        person_form = personform()  
        employee_form = employeeform()  

    return render(request, 'employee-create.html', {
        'person_form': person_form, 
        'employee_form': employee_form
    })

def employee_edit(request, id):
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
        person_form = personform(instance=person_obj)
        employee_form = employeeform(instance=employee_obj)

    return render(request, 'employee-edit.html', {
        'employee': employee_obj, 
        'person_form': person_form, 
        'employee_form': employee_form
    })

def employee_view(request, id):
    employee_obj = get_object_or_404(employee, id=id)
    return render(request, 'employee-view.html', {'employee': employee_obj})



