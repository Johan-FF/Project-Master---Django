from django.db import models
from employee.models import Employee

class Meeting(models.Model):
    name = models.CharField(max_length=80)
    time = models.TimeField()
    place = models.CharField(max_length=200)
    description = models.TextField()
    participants = models.ForeignKey(Employee, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

