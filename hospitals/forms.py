from hospitals.models import Contact,Appointmentuser
from django import forms

class MyForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Contact.objects.all())

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointmentuser
        fields="__all__"