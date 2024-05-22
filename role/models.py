from django.db import models
from organization.models import Organization

class Role(models.Model):
    role_name = models.CharField(max_length=50)
    description = models.TextField()
    permissions = models.CharField(max_length=50, choices=[
        ('admin', 'Administrar roles y usuarios'),
        ('coordinator', 'Administrar roles, proyectos y tareas'),
        ('employee', 'Interactuar con la aplicacion'),
    ])
    role_organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
