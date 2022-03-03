from dataclasses import field
from tkinter import Widget
from .models import VehicalRequest
from django import forms


class VehicalRequestForm(forms.ModelForm):
    class Meta:
        model  = VehicalRequest
        fields = '__all__'
        exclude = ('UserId', 'RequestDate','VehicalId', 'Status')
        widgets = {
            'StartDate': forms.DateInput(attrs={
                'type':'date',
                'placeholder': 'Enter your First name'
            }),
        
            'EndDate': forms.DateInput(attrs={
                'type':'date',

                    'placeholder': 'Enter your Last name',
                }),

            'Pickup': forms.TextInput(attrs={
                    'placeholder': 'Enter your Last name',
                }),

            'Drop': forms.TextInput(attrs={
                    'placeholder': 'Enter your Last name',
                }),



        }
