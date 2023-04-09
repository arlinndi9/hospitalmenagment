from hospitals.models import Contact
from django import forms

class MyForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Contact.objects.all())