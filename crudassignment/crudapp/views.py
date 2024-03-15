from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Player


@login_required
def home(request):
    return render(request,"index.html")

def addplayer(request):


    Name=request.POST['name']
    Country=request.POST['country']
    playobj=Player(name=Name,country=Country)
    playobj.save()
    return render(request,"index.html",{"msg":"Player added"})

def display(request):
    playdtls=Player.objects.all()
    return render(request,"index.html",{'play':playdtls})


def delplayer(request):
    playname=request.POST['name']
    playdtls=Player.objects.filter(name=playname)
    if playdtls.exists():
        playdtls.delete()
        return render(request,"index.html",{'msg':"deleted"})
    else:
        return render(request,"index.html",{'msg':"no records found"})

def updatename(request):
    try:
        oldname=request.POST["oldname"]
        newname=request.POST["newname"]
        play=Player.objects.filter(name=oldname)
        if play.exists():
            play.update(name=newname)
            return render(request,"index.html",{'msg1':"Updated"})
        else:
            return render(request,"index.html",{'msg1':"No records found"})
    except Exception as e:
        print(e)
        return render(request,"index.html",{'msg1':"Not updated"})

def loginview(request):
    uname=request.POST['username']
    pwd=request.POST['password']
    user=authenticate(request,username=uname,password=pwd)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        return render(request,"login.html",{"msg":"Invalid login"})

def logout_view(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    try:
        form = UserCreationForm(request.POST)
        if request.method == "POST":
            if form.is_valid():   
                form.save() 
                return redirect('login')  
            return render(request, 'sign_up.html', {'form': userform,'msg':'Invalid login'})
                         
        else:
            return render(request, 'sign_up.html', {'form': userform,'msg':'Invalid login'})
    except Exception as e:
            print(e)
            userform = UserCreationForm()
            return render(request, 'sign_up.html', {'form': userform})
    







