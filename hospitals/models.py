from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import date

# Create your models here.

class Doctor(models.Model):
    specializimet = (
        ('General medicine', 'General medicine'),
        ('Dentistry','Dentistry'),
        ('Physiotherapy','Physiotherapy'),
        ('Nursing ','Nursing '),
    )
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    special = models.CharField(max_length=255, choices=specializimet,default='')
    photo=models.ImageField(upload_to='static/images',null=True)

    def __str__(self):
       return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(validators=[MaxValueValidator(10)],null=True)
    address = models.CharField(max_length=50)

    def __str__(self):
       return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
       return self.doctor.name+"--"+self.patient.name

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.IntegerField(null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)

    def __str__(self):
        return self.name

class Appointmentuser(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=255,null=True)
    lastname=models.CharField(max_length=255,null=True)
    email=models.EmailField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.doctor.name+"--"+self.firstname