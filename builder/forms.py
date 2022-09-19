from re import TEMPLATE
from django import forms
from django.forms import ModelForm

from .models import *

class TemplateForm(forms.ModelForm):
    
    class Meta:
        model = Template
        fields = ['thumbnails']
