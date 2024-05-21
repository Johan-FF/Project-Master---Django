from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=50)
    description = models.TextField()
    permissions = models.CharField(max_length=50, choices=[
        ('Admin', 'Administrar roles y usuarios'),
        ('Coordinador', 'Administrar roles, proyectos y tareas'),
        ('Empleado', 'Interactuar con la aplicacion'),
    ])
