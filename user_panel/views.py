from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.urls import reverse
from .forms import *
from user_panel.models import *

# Create your views here.

def home(request):
    return render(request, 'user_panel/home.html')


def Available_Vehical(request):
    # data = Vehical_Registration.objects.all().exclude(UserId=request.user.id)
    types = VehicalType.objects.all()
    data = Vehical_Registration.objects.filter(Status="Accepted").exclude(UserId=request.user.id)
    return render(request, 'user_panel/Available_Vehical.html', {'data' : data, 'types' : types })


def type_wise_filter_in_userpanel(request,id):
    data = Vehical_Registration.objects.filter(Vahical_Type=id)
    types = VehicalType.objects.all()
    return render(request, 'user_panel/Available_Vehical.html', {'data' : data, 'types': types})



def Rent_Request(request, id):
    
    r_vehicale=Vehical_Registration.objects.get(id=id)
    if request.method == 'POST':
        form = VehicalRequestForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.UserId=request.user
            data.VehicalId=r_vehicale
            data.save()
            return HttpResponseRedirect(reverse('user_panel:home'))
        else:
            print(form.errors)
    else:
        form = VehicalRequestForm()
        abcd = VehicalRequest.objects.all()
    return render(request, 'user_panel/Rent_Request.html', {'form': form, 'data' : abcd, 'r_vehicale' : r_vehicale })


