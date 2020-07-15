from django.db import models

class NesclassModel(models.Model):
    cid=models.IntegerField(default=0)
    name=models.CharField(max_length=49)
    faculty=models.CharField(max_length=49)
    date = models.DateField()
    time =models.TimeField()
    fee = models.IntegerField()
    duration= models.IntegerField()

class StudentMOdel(models.Model):
    si=models.IntegerField(auto_created=True,default=0)
    name=models.CharField(max_length=38)
    contactno=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=45)

class EnrokedCourseModel(models.Model):
    cn=models.ManyToManyField(NesclassModel,default=0)
    sid=models.OneToOneField(StudentMOdel,on_delete=models.CASCADE)

