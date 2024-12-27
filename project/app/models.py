from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    DepartmentName = models.CharField(max_length=100,primary_key=True)
    HeadOfDepartment = models.CharField(max_length=100)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    class Meta:
      verbose_name = "Department"
      verbose_name_plural = "Department"
    def __str__(self):
        return self.DepartmentName
    
class Instructor(AbstractUser):
    FirstName = models.CharField(max_length=100,null=True)
    MiddleName = models.CharField(max_length=100,null=True)
    LastName = models.CharField(max_length=100,null=True)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    RegisteredDate = models.DateTimeField(auto_now_add=True)
    class Meta:
      verbose_name = "Instructor"
      verbose_name_plural = "Instructor"
    def __str__(self):
        return self.username