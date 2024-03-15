from django.shortcuts import render
def home(request):
    return render(request,'voting.html')



def eligibility(request):
    age=int(request.POST['age'])
    if age>=18:
        res="congraulations, you have the ability to vote"
    else:
        res="unlucky, you haven't the ability to vote"
    return render(request,'voting.html',{'res':res})

