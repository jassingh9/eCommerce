from django import forms
from django.forms import ModelForm
from models import Item


class AddProduct(forms.Form):
    
    fields = ['name', 'image', 'description', 'quantity', 'price', 'category']
