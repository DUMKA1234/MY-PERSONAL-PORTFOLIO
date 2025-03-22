from django.urls import path
from . import views
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

urlpatterns=[
   
    path('portfolio/', views.portfolio,name='portfolio'), 
    
    
]
