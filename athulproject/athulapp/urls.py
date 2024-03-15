from django.urls import path
from .import views

urlpatterns = [
    path('',views.show),
    path('dis',views.displayname,name='display')
]