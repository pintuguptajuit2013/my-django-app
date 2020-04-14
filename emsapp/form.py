from django import forms  
from emsapp.models import Student  
  
class StuForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  
        
        
class DepartmentForm(forms.Form):  
    departmentname = forms.CharField(label="Enter Department Name",max_length=50)  
    buildingname  = forms.CharField(label="Enter Building Name", max_length = 100)  
    
    
from django import forms  
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input  