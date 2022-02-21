from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .models import Doctor, Vaccinations,report,appointment,bookvac
from . import forms

# Create your views here.
def index(request):
    return render(request,'index.html')

def reports(request):
    #reps=report.objects.all()
    reps=report.objects.filter(user=request.user)
    return render(request,"report.html",{'reps':reps})

def about(request):
    return render(request,'about.html')

def doctor(request):
    docs=Doctor.objects.all()
    return render(request,'doctor.html',{'docs':docs})

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        sub=request.POST['subject']
        mail=request.POST['email']
        to=["hospital@gmail.com"]
        message=request.POST['message']
        subject = "User Tried to Contact"
        email_template_name = "contact_info_mail.txt"
        c = {
        "email":mail,
        'domain':'127.0.0.1:8000',
        'site_name': 'Website',
        "user": name,
        "sub": sub,
        'msg':message,
        }
        email = render_to_string(email_template_name, c)
        try:
            send_mail(subject, email, 'dbmsprojekt@gmail.com' , ['manvik55@gmail.com'], fail_silently=False)
            messages.info(request,"Your Query has been sent!")
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('contact')
    else:
        return render(request,"contact.html")

def services(request):
    return render(request,'services.html')

def appoint(request):
    docs=Doctor.objects.all()
    #form=forms.appointment()    
    if request.method=='POST':
        name=request.POST['fullname']
        email=request.POST['email']
        phone=request.POST['phone']
        date=request.POST['date']
        dept=request.POST.get('dept')
        doc=request.POST.get('doct')
        doctor=Doctor.objects.get(id=doc)
        a=appointment(doctor=doctor,patient_name=name,date=date,specialization=dept,patient_email=email,patient_phone=phone)
        a.save()
        messages.info(request,"Your appointment is booked!")
        return redirect("appoint")
    else:
        return render(request,"appointment.html",{'docs':docs})

def vaccine(request):
    vacs=Vaccinations.objects.all()
    if request.method=='POST':
        name=request.POST['fullname']
        email=request.POST['email']
        phone=request.POST['phone']
        date=request.POST['date']
        vac=request.POST.get('vacc')
        vacc=Vaccinations.objects.get(id=vac)
        a=bookvac(vaccinations=vacc,patient_name=name,date=date,patient_email=email,patient_phone=phone)
        a.save()
        vacc.quantity-=1
        vacc.save()
        messages.info(request,"Your vaccine is booked!")
        return redirect("vaccine")
    else:
        return render(request,"vaccine.html",{'vacs':vacs})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Incorrect username or password")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')