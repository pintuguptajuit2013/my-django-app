
from __future__ import unicode_literals  
from django.db import models  
from django import forms    

    
# Create your models here.    
    
class Student(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    contact    = models.IntegerField()  
    email      = models.EmailField(max_length=50)  
    age        = models.IntegerField() 
    file      = forms.FileField() # for creating file input  
    class Meta:  
       db_table = "student"
      