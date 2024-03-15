from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'calculator.html')

def calculation(request):
    num1=request.POST[num1]

