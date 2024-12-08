from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee-list/', views.employee_list, name='employee'),
    path('employee-create/', views.employee_create, name='employee-create'),
    path('employee-edit/', views.employee_edit, name='employee-edit'),
    path('employee-view/', views.employee_view, name='employee-view')
]