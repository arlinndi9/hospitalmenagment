from hospitals.views import *
from django.urls import path
urlpatterns = [
    path('about/', About, name="about"),
    path('', Index, name='index'),
    path('contact/', contact, name='contact'),
    path('login', adminlogin, name='login'),
    path('admin_home', admin_home, name='admin_home'),
    path('logout', logout_view, name='logout_view'),
    path('add_doctor', add_doctor, name='add_doctor'),
    path('view_doctor', view_doctor, name='view_doctor'),
    path('delete_doctor/<int:pid>', Delete_Doctor, name='delete_doctor'),
    path('add_patient', add_patient, name='add_patient'),
    path('view_patient', view_patient, name='view_patient'),
    path('delete_patient/<int:pid>', Delete_Patient, name='delete_patient'),
    path('add_appointment', add_appointment, name='add_appointment'),
    path('view_appointment', view_appointment, name='view_appointment'),
    path('delete_appointment/<int:pid>', Delete_Appointment, name='delete_appointment'),
    path('edit_doctor/<int:pid>', edit_doctor, name='edit_doctor'),
    path('edit_patient/<int:pid>', edit_patient, name='edit_patient'),
    path('read_queries', read_queries, name='read_queries'),
    path('view_queries/<int:pid>', view_queries, name='view_queries'),
]
