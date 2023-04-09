from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from .models import *
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def About(request):
    return render(request,'about.html')

def Index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        Contact.objects.create(name=n, contact=c, email=e, subject=s, message=m, msgdate=date.today())
    return render(request, 'contact.html', locals())

def adminlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'login.html', locals())

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    dc = Doctor.objects.all().count()
    pc = Patient.objects.all().count()
    ac = Appointment.objects.all().count()

    d = {'dc': dc, 'pc': pc, 'ac': ac}
    return render(request,'admin_home.html', d)

def logout_view(request):
    logout(request)
    return redirect('index')

def add_doctor(request):

    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':

        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        special = request.POST.get('special')

        if len(mobile)>9:
            messages.error(request,'the number is big')
            return redirect('add_doctor')

        doctor=Doctor.objects.create(name,mobile,special)
        doctor.name=name
        doctor.mobile=mobile
        doctor.special=special
        doctor.save()
    return render(request,'add_doctor.html')

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html', d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def edit_doctor(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    doctor = Doctor.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        s1 = request.POST['special']
        if len(m1) > 9:
            messages.error(request, 'the number is big')
        doctor.name = n1
        doctor.mobile = m1
        doctor.special = s1

        try:
            doctor.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_doctor.html',{'doctor':doctor})

def add_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST.get('name')
        g = request.POST.get('gender')
        m = request.POST.get('mobile')
        a = request.POST.get('address')

        if len(m)>9:
            messages.error(request,'error')
            return redirect('add_patient')
        else:
            patient = Patient.objects.create(name=n,gender=g,mobile=m,address=a)
            patient.save()
            messages.success(request, 'Patient added successfully')
    return render(request,'add_patient.html')

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html', d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient.html')

def edit_patient(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    patient = Patient.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        g1 = request.POST['gender']
        a1 = request.POST['address']

        patient.name = n1
        patient.mobile = m1
        patient.gender = g1
        patient.address = a1
        try:
            patient.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_patient.html', locals())



def add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
            error="no"
        except:
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html', d)

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    d = {'appointment':appointment}
    return render(request,'view_appointment.html', d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment1 = Appointment.objects.get(id=pid)
    appointment1.delete()
    return redirect('view_appointment.html')

def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="no")
    return render(request,'unread_queries.html', locals())

def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.all()
    return render(request,'read_queries.html', {'contact':contact})

def view_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.get(id=pid)
    contact.save()
    return render(request,'view_queries.html')

