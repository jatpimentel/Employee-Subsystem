from django.db import models

# Create your models here.

class person (models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
       return self.first_name + ' ' + self.last_name
    
class role (models.Model):
    role_name = models.CharField(max_length=255)
    role_type = models.CharField(max_length=255,default="onsite")
    role_status = models.CharField(max_length=255,default="active")

    def __str__(self):
        return self.role_name

class employee (models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    EMPLOYEE_STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Not Active'),
    ]
    
    person = models.ForeignKey(person, on_delete=models.CASCADE, blank=True, null=True)
    role = models.ForeignKey(role, on_delete=models.CASCADE, blank=True, null=True)
    pin = models.PositiveIntegerField()
    employee_status = models.CharField(
        max_length=8,
        choices=EMPLOYEE_STATUS_CHOICES,
        default=ACTIVE,
    )

    def __str__(self):
      return self.person.first_name + ' ' +self.person.last_name + ' --- ' +self.role.role_name
    
class access_rights (models.Model):
    role = models.ForeignKey(role, on_delete=models.CASCADE, blank=True,null=True)
    feature_name = models.CharField(max_length=255)

    def __str__(self):
        return self.feature_name


