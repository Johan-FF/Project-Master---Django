from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=50)
    description = models.TextField()
    permissions = models.CharField(max_length=50, choices=[
        ('admin', 'Administrar roles y usuarios'),
        ('coordinator', 'Administrar roles, proyectos y tareas'),
        ('employee', 'Interactuar con la aplicacion'),
    ])
