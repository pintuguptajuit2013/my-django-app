from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")



import datetime  
# Create your views here.  
from django.http import HttpResponse  
def currenttime(request):  
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    return HttpResponse(html)    # rendering the template in HttpResponse  
    
    
from django.shortcuts import render  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse, HttpResponseNotFound  
def index(request):  
   template = loader.get_template('index.html') # getting our template  
   name = {  
        'student':'Pintu Gupta'  
   }  
   return HttpResponse(template.render(name))       # rendering the template in HttpResponse  
        
        
from django.shortcuts import render  
# Create your views here.  
from django.http import HttpResponse, HttpResponseNotFound  
from django.views.decorators.http import require_http_methods  
@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')  
    
    
from django.shortcuts import render  
from emsapp.form import StuForm  
  
def registration(request):  
    stu = StuForm()  
    return render(request,"student.html",{'form':stu})
    
from emsapp.form import DepartmentForm     
def department(request):  
    dep = DepartmentForm()  
    return render(request,"department.html",{'form':dep})      

from django.shortcuts import render  
from django.http import HttpResponse  
from emsapp.functions.functions import handle_uploaded_file  
from emsapp.form import StudentForm  
def fileupload(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"fileupload.html",{'form':student})  
        
from emsapp.form import DepartmentForm 
from django.core.exceptions  import  ObjectDoesNotExist   
def getdata(request):  
    try:  
        dep = DepartmentForm() 
        data = dep.objects 
    except ObjectDoesNotExist:  
        return HttpResponse("Exception: Data not found")  
    return HttpResponse(data); 

from django.shortcuts import render  
from django.http import HttpResponse  
def setsession(request):  
    request.session['sname'] = 'irfan'  
    request.session['semail'] = 'irfan.sssit@gmail.com'  
    return HttpResponse("session is set")  
def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail);  


from django.shortcuts import render  
from django.http import HttpResponse  
  
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    return response  
def getcookie(request):  
    tutorial  = request.COOKIES['java-tutorial']  
    return HttpResponse("java tutorials @: "+  tutorial);  
    
    
import csv  
     
def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    return response  

from emsapp.form import StuForm  
import csv  
def getStudent(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    students = StuForm.objects.all()  
    writer = csv.writer(response)  
    for student in students:  
        writer.writerow([student.first_name,student.last_name,student.contact,student.email,student.age])  
    return response  


from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
  
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Javatpoint.")  
    p.showPage()  
    p.save()  
    return response
    
    
from django.shortcuts import render  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse, HttpResponseNotFound  
def userLogin(request):  
   template = loader.get_template('login.html') # getting our template  
   return HttpResponse(template.render())       # rendering the template in HttpResponse  
