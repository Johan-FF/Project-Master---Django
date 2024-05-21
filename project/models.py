from django.db import models
from employee.models import Employee
from task.models import Task

class Project(models.Model):
    project_name = models.CharField(max_length=80)
    description = models.TextField()
    participants = models.ManyToManyField(Employee)
