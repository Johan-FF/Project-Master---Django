from django.db import models

class Organization(models.Model):
  company_name = models.CharField(max_length=50)
  industry = models.CharField(max_length=50)
  employees_number = models.IntegerField()
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  postal_code = models.IntegerField()
  phone = models.CharField(max_length=15)
  admin = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
