from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request,'index.html')

def staff(request):
    return HttpResponse('This is the Staff Page')