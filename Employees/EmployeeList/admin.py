from django.contrib import admin
from .models import person,role,employee,access_rights

# Register your models here.

admin.site.register(person)
admin.site.register(role)
admin.site.register(employee)
admin.site.register(access_rights)
