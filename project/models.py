from django.db import models
from employee.models import Employee
from task.models import Task
from organization.models import Organization

class Project(models.Model):
    project_name = models.CharField(max_length=80)
    description = models.TextField()
    participants = models.ManyToManyField(Employee)
    tasks = models.ManyToManyField(Task)
    project_organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
