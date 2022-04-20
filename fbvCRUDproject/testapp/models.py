from django.db import models

# Create your models here.
class Student(models.Model):
    srollno=models.IntegerField()
    sname=models.CharField(max_length=30)
    smarks=models.FloatField()
    saddress=models.CharField(max_length=100)
