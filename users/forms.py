from django import forms
from .models import *
from django.forms import ModelForm
class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')

class RegistraionForm(ModelForm):
    class Meta:
        model=JobPortal
        fields=['companyname','jTitle','location','jobDescription','expectedSalary','dp']