from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return render(request,'pages/index.html',{'name':'ahmed','age':25})

def about (request):
    return render(request,'pages/about.html',{'name':'ahmed','age':25})

     
    
    
