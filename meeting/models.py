from django.db import models
from employee.models import Employee

class Meeting(models.Model):
    subject = models.CharField(max_length=80)
    meetTime = models.TimeField()
    place = models.CharField(max_length=200)
    description = models.TextField()
    participants = models.ManyToManyField(Employee)


    def __str__(self):
        return self.name

