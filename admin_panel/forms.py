from dataclasses import field
from tkinter import Widget
from .models import VehicalType,brand,category_list
from django import forms


class VehicalTypeForm(forms.ModelForm):
    class Meta:
        model  = VehicalType
        fields = '__all__'
        exclude = ('added_date',)

class brandform(forms.ModelForm):
    class Meta:
        model  = brand
        fields = '__all__'
        exclude = ('AddDate','UserId')

class category_listform(forms.ModelForm):
    class Meta:
        model  = category_list
        fields = '__all__'
        exclude = ('AddDate','UserId')
