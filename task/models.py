from django.db import models
from employee.models import Employee

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    comments = models.TextField()
    delivery_date = models.DateField()
    tied_project = models.ForeignKey('project.Project', on_delete=models.CASCADE)
    associated_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    state = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ])

    def __str__(self):
        return self.name
