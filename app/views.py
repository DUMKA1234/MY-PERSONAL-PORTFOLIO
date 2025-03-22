from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render


# Create your views here.
def homepage(request):
    return render(request,'index.html')
def portfolio(request):
    return render(request,'portfolio.html')

 
 
 

#student form
def homepage(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('success')
            except:
                pass
    else:
        form = StudentForm()
        return render(request,'index.html',{"form":form})
    
def success(request):
    return HttpResponse({"message: success"})



def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        phonenumber = request.POST.get('phonenumber')
        message = request.POST.get('message')
       

        if address and subject and message:
            try:
                send_mail(name,phonenumber,subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "feature.html", context)
def send_email(request):
    send_mail('Request Callback', 'Here is the message.', 'sendernkuedumka@gmail.com',
        # ['recipientnkuedumka@gmail.com@gmail.com'] 
        fail_silently=False)
    msg.send()
    return HttpResponseRedirect('/')

def send_message(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        email_address = request.POST.get('email_address')
        email_subject = request.POST.get('email_subject')
        message = request.POST.get('message')

        send_mail(
            email_subject,
            f"Full Name: {full_name}\nPhone Number: {phone_number}\nEmail Address: {email_address}\nMessage: {message}",
            email_address,
            ['nkuedumka@gmail.com'],
            fail_silently=False,
        )

        return redirect('success')
    return render(request, 'feature.html')