from django import forms
from .models import person,employee,access_rights,role

class personform(forms.ModelForm):
    class Meta:
        model = person
        fields = ['username', 'first_name', 'last_name', 'contact_number', 'email']

class employeeform(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['person', 'role', 'pin', 'employee_status']