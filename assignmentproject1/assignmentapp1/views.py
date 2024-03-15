from django.shortcuts import render
from django.http import HttpResponse

 
def home(request):
    return render(request,"index.html")

def sum(request):
    num1=request.GET['num1']
    num2=request.GET['num2']
    res=int(num1)+int(num2)
    return render(request,"index.html",{'result':res})
