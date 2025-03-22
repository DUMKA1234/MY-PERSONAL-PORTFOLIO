from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render


# Create your views here.

def portfolio(request):
    return render(request,'portfolio.html')

 
 
 

