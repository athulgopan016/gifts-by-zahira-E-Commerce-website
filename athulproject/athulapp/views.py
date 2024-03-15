from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show(request):
    return render(request,'home.html')
def index(request):
    return HttpResponse("Index page")
def displayname(request):
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    res =  firstname + "" +  lastname
    return render(request,'home.html',{'name':res})