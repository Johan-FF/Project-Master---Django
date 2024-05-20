from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    #Roles 

    def __str__(self):
        return self.nombre
