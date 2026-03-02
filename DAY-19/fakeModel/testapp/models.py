from django.db import models

# Create your models here.
class Student(models.Model):


    rollno = models.IntegerField()
    name = models.CharField(max_length=40)
    course = models.CharField(max_length=80)
    date = models.DateField()