from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash

from .forms import AppointmentForm
from .models import *
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def About(request):
    return render(request,'about.html')

def Index(request):
    doctor=Doctor.objects.all()
    context={
        'doctor':doctor
    }
    return render(request,'index.html',context)
@login_required()
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
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_home')
            else:
                login(request, user)
                return redirect('index')
        else:
            error = "yes"
    return render(request, 'login.html', {'error': error})
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    dc = Doctor.objects.all().count()
    pc = Patient.objects.all().count()
    ac = Appointmentuser.objects.all().count()

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

        doctor=Doctor.objects.create(name=name,mobile=mobile,special=special)
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
    return redirect('view_patient')

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



# def add_appointment(request):
#     error=""
#     if not request.user.is_staff:
#         return redirect('login')
#     doctor1 = Doctor.objects.all()
#     if request.method == 'POST':
#         d = request.POST['doctor']
#         fname = request.POST['fname1']
#         lname = request.POST['lname1']
#         email = request.POST['email1']
#         date = request.POST['date']
#         time = request.POST['time']
#         doctor = Doctor.objects.filter(name=d).first()
#         Appointmentuser.objects.create(doctor=doctor, firstname=fname, lastname=lname, email=email, date=date,
#                                        time=time)
#         messages.success(request, "Your appointment is successfully created")
#         return redirect('create_appointment')
#
#     return render(request, 'add_appointment.html', {'doctors': doctor1})

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointmentuser.objects.all()
    d = {'appointment':appointment}
    return render(request,'view_appointment.html', d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment1 = Appointmentuser.objects.get(id=pid)
    appointment1.delete()
    return redirect('view_appointment')


def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.all()
    return render(request,'read_queries.html', {'contact':contact})

def delete_contact(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    contact1=Contact.objects.get(id=id)
    contact1.delete()
    return redirect('read_queries')



def signup(request):
        if request.method == 'POST':
            # get the post parameters#
            username = request.POST['username']
            fname = request.POST['fname1']
            lname = request.POST['lname1']
            email = request.POST['email1']
            password1 = request.POST['password2']
            password2 = request.POST['password4']

            errors = {}
            if len(username) > 10:
                errors['username'] = "Username must be under 10 characters"
            if not username.isalnum():
                errors['username'] = "Username must contain only letters and numbers"
            if password1 != password2:
                errors['password'] = "Passwords do not match"
            if User.objects.filter(username=username).exists():
                errors['username'] = "Username already exists"

            # if there are errors, display them and don't create the user
            if errors:
                return render(request, 'signup.html', {'errors': errors})

            myuser = User.objects.create_user(username, email, password1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your account is successfully created")
            return redirect('login')

        else:
            return render(request,'signup.html')

def create_appointment(request):
    doctor1 = Doctor.objects.all()
    if request.method == 'POST':
        d = request.POST['doctor']
        fname = request.POST['fname1']
        lname = request.POST['lname1']
        email = request.POST['email1']
        date = request.POST['date']
        time = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        Appointmentuser.objects.create(doctor=doctor, firstname=fname,lastname=lname,email=email, date=date,time=time)
        messages.success(request, "Your appointment is successfully created")
        return redirect('create_appointment')

    return render(request, 'create_appointment.html', {'doctors': doctor1})


@login_required
def user_appointments(request):
    user_email = request.user.email
    user_appointments = Appointmentuser.objects.filter(email=user_email).order_by('date', 'time')
    print('User email:', user_email)
    context = {'appointments': user_appointments,'user_email': user_email}
    return render(request, 'user_appointments.html', context)

@login_required
def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request,'change_password.html')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

# def set_cookies(request):
#     response=HttpResponse('cookies create sucesfully')
#     response.set_cookie('is_logged_in','yes',max_age=30)
#     return response
#
# def get_cookies(request):
#     return HttpResponse('is logged in'+request.COOKIES.get('is_logged_in'))


def edit_appointmentuser(request, pk):
    appointmentuser = get_object_or_404(Appointmentuser, pk=pk)
    if request.method == 'POST':
        appointmentuser.firstname = request.POST.get('firstname')
        appointmentuser.lastname = request.POST.get('lastname')
        appointmentuser.email = request.POST.get('email')
        appointmentuser.date = request.POST.get('date')
        appointmentuser.time = request.POST.get('time')
        appointmentuser.save()
        return redirect('appointmentuser_detail', pk=pk)
    else:
        return render(request, 'editappointment.html', {'appointmentuser': appointmentuser})

def delete_appointment_user(request,pk):
    appointment1 = Appointmentuser.objects.get(id=pk)
    appointment1.delete()
    return redirect('user_appointments')