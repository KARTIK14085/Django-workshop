from django.db import models

# Create your models here.
class student(models.Model):
    sname=models.CharField("name" ,max_length=20)
    email=models.EmailField("email" ,max_length=20)
    mobile=models.CharField("mobile", max_length=10)
    address=models.TextField("address", max_length=10)

def  __str__(self):
    return self.name