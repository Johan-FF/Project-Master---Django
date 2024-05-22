from django.db import models

class LoginUser(models.Model):
  password = models.CharField(max_length=30)
  email = models.CharField(max_length=30)