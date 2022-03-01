from dataclasses import field
from django import forms
from .models import User

class UserloginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'Mobile_Number', 'Pincode')
       

class ownerloginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',)