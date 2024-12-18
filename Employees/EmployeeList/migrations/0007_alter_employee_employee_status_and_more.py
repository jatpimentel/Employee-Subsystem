# Generated by Django 5.1.4 on 2024-12-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeList', '0006_rename_contact_numer_person_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Not Active')], default='active', max_length=8),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_status',
            field=models.CharField(default='active', max_length=255),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_type',
            field=models.CharField(default='onsite', max_length=255),
        ),
    ]
