from django.db import models

class Meeting(models.Model):
    name = models.CharField(max_length=80)
    time = models.TimeField()
    place = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    participants = models.ManyToManyField('Employee', related_name='personas_invitadas')

    def __str__(self):
        return self.name

