from django import forms


class Employee_form(forms.Form):
    name=forms.CharField(max_length=25)
    age=forms.IntegerField()
    dept=forms.CharField(max_length=30)
    salary=forms.IntegerField()
    branch=forms.CharField(max_length=20)