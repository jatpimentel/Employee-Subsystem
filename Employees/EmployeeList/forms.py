from django import forms
from .models import person,employee

class personform(forms.ModelForm):
    class Meta:
        model = person
        fields = ['username', 'first_name', 'last_name', 'contact_number', 'email']

class employeeform(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['person', 'pin', 'employee_status']