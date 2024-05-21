from django.db import models
from role.models import Role
from organization.models import Organization

class Employee(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete= models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def _str_(self):
        return self.name
