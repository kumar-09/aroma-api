from django import forms
from django.db import models  
from django.forms import fields
from main.models import menu

class menuaddform(forms.ModelForm):
    class Meta:
        model=menu
        fields=['id','name','price','image','food_id']
