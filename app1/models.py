from django.db import models

class NesclassModel(models.Model):
    name=models.CharField(max_length=49)
    faculty=models.CharField(max_length=49)
    date = models.DateField()
    time =models.TimeField()
    fee = models.IntegerField()
    duration= models.IntegerField()

class StudentMOdel(models.Model):
    name=models.CharField(max_length=38)
    contactno=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=45)