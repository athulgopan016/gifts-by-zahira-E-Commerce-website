from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    return render(request,"index.html")

def addemployee(request):
    Name=request.POST['name']
    Address=request.POST['address']

    empobj=Employee(name=Name,address=Address)
    empobj.save()
    return render(request,"index.html",{"msg":"Employee added"})



def display(request):
    empdtls=Employee.objects.all()
    return render(request,"index.html",{'emp':empdtls})

def delemployee(request):
    empname=request.POST['name']
    empdtls=Employee.objects.filter(name=empname)
    empdtls.delete()
    return render(request,'index.html',{"msg":"Deleted"})

def updatename(request):
    try:
        oldname=request.POST["oldname"]
        newname=request.POST["newname"]
        emp=Employee.objects.filter(name=oldname)
        if emp.exists():
            emp.update(name=newname)
            return render(request,"index.html",{'msg1':"Updated"})
        else:
            return render(request,"index.html",{'msg1':"No records found"})
    except Exception as e:
        print(e)
        return render(request,"index.html",{'msg1':"Not updated"})

def loginview(request):
    uname=request.POST['username']
    pwd=request.POST['password']
    user=authenicate(request,username=uname,password=pwd)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        return render(request,"login.html",{"msg":"Invalid login"})

def logout_view(request):
    logout(request)
    return redirect('login')






    