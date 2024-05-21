from django.db import models
from employee.models import Employee

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    comments = models.TextField()
    delivery_date = models.DateField()
    tied_project = models.ForeignKey('project.Project', on_delete=models.CASCADE)
    associated_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    state = models.CharField(max_length=50, choices=[
        ('Pendiente', 'pendiente'),
        ('En Progreso', 'en_progreso'),
        ('Completada', 'completada'),
    ])
