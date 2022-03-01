from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from admin_panel.models import *
from django.urls import reverse
from owner_panel.forms import *

# from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "owner_panel/home.html")


def Rent_Vehical(request):
    if request.method == 'POST':
        form = Vehical_Registration_owner_form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.UserId=request.user
            data.save()
            return HttpResponseRedirect(reverse('owner_panel:Rent_Vehical'))
        else:
            print(form.errors)
    else:
        form = Vehical_Registration_owner_form()
        data = Vehical_Registration.objects.all()
    return render(request, 'owner_panel/Rent_Vehical.html', {'form': form, 'data' : data})