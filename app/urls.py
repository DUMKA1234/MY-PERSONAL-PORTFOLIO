from django.urls import path
from . import views
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

urlpatterns=[
    path('homepage/', views.homepage,name='homepage'),
    path('portfolio/', views.portfolio,name='portfolio'),
    path('feature/', views.feature, name='feature'),
   path('dumka/', views.dumka, name='dumka'),
   
    path('feature/', views.feature,name='feature'), 
    path('success/', views.success,name='success') , 
    path('kpea/', views.kpea,name='kpea'), 
    path('nk/', views.nk,name='nk'), 
    
    
]
# send_mail_page