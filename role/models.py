from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    roles = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]) 

    def __str__(self):
        return self.nombre
