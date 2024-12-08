from django.shortcuts import render
from django.http import HttpResponse
from .models import person,role,employee,access_rights
# Create your views here.
def index(request):
    return render (request,'index.html')

def employee_list(request):
    all_employees = employee.objects.all
    return render (request,'employee-list.html', {'employees':all_employees})

def employee_create(request):
    return render (request,'employee-create.html')

def employee_edit(request):
    return render (request, 'employee-edit.html')

def employee_view(request):
    return render (request, 'employee-view.html')