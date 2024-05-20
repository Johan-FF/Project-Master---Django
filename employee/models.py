from django.db import models
from role.models import Role

class Employee(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    ID = models.BigIntegerField(unique=True)
    # Role would be here, but we need to set them.

    def _str_(self):
        return self.name
