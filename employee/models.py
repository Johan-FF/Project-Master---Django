from django.db import models
from role.models import Role
from organization.models import Organization

class Employee(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    identification = models.CharField(max_length=15)
    role = models.ForeignKey(Role, on_delete= models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
