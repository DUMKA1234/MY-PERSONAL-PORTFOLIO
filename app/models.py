from django.db import models

# Create your models here.
class students(models.Model):
    students_id= models.AutoField(primary_key=True)
    students_name=models.CharField(max_length=50)
    students_email=models.EmailField()
    gender=models.CharField(max_length=20)

class school(models.Model):
    students_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location= models.CharField(max_length=60)

class course(models.Model):
    students_id =models.ForeignKey(students,on_delete=models.CASCADE)
    courseid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

class post(models.Model):
    phonenumber= models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=200)
    
    
