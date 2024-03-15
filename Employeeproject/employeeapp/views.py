from django.shortcuts import render
from .forms import Employee_form

def home(request):
    form = Employee_form()
    return render(request,'employee.html',{'employee_form':form})

def show(request):
    form=Employee_form
    if request.method=="POST":
        form=Employee_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            dept = form.cleaned_data['dept']
            salary = form.cleaned_data['salary']
            branch = form.cleaned_data['branch']
            return render(request,'show.html',{'name':name,'age':age,'dept':dept,'salary':salary,'branch':branch})
    else:
        return render(request,'employee.html',{'employee_form':form})





