from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()
    
    def __str__(self):
        return self.name



class Internship(models.Model):
    fullname=models.CharField(max_length=60)
    usn=models.CharField(max_length=60)
    email=models.EmailField()
    college_name=models.CharField(max_length=160)
    offter_status=models.CharField(max_length=60)
    start_date=models.DateField()
    end_date=models.DateField()
    proj_report=models.CharField(max_length=60)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.fullname

    