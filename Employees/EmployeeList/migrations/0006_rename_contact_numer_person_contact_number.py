# Generated by Django 5.1.4 on 2024-12-08 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeList', '0005_rename_role_id_employee_role_access_rights'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='contact_numer',
            new_name='contact_number',
        ),
    ]
