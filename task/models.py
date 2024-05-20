from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    Comments = models.TextField(blank=True, null=True)
    delivery_date = models.DateField()
    empleado_asignado = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='tareas_asignadas')
    state = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ])

    def __str__(self):
        return self.name
