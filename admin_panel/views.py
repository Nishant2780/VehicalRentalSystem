from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from django.contrib.auth import authenticate, login, logout


from django.contrib import messages
from .models import *
from django.urls import reverse
from .forms import *


# Create your views here.

def home(request):
    return render(request, 'admin_panel/home.html')

def create_type(request):
    if request.method == 'POST':
        form = VehicalTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_panel:create_type'))
        else:
            print(form.errors)
    else:
        form = VehicalTypeForm()
        data = VehicalType.objects.all()
    return render(request, 'admin_panel/vehical_type.html', {'form': form, 'data' : data})


def updatetype(request, id):
    details = VehicalType.objects.get(id=id)
    form_v = VehicalTypeForm(instance=details)
    if request.method == "POST":
        form_v = VehicalTypeForm(request.POST, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:create_types")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/vehical_type.html", {'form' : form_v})


def deletetype(request, id):
  details = VehicalType.objects.get(id=id)
  details.delete()
  return redirect("admin_panel:create_type")




def addbrand(request):
    if request.method == 'POST':
        form = brandform(request.POST, request.FILES)
        if form.is_valid():
            
            data = form.save(commit=False)
            data.UserId=request.user
            data.save()
            return HttpResponseRedirect(reverse('admin_panel:addbrand'))
        else:
            print(form.errors)
    else:
        form = brandform()
        form = brandform()
        data = brand.objects.all()
    return render(request, 'admin_panel/vehical_brand.html', {'form': form,  'data' : data})



def updatebrand(request, id):
    details = brand.objects.get(id=id)
    form_v = brandform(instance=details)
    if request.method == "POST":
        form_v = brandform(request.POST, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:addbrand")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/vehical_brand.html", {'form' : form_v})


def deletebrand(request, id):
  details = brand.objects.get(id=id)
  details.delete()
  return redirect("admin_panel:addbrand")



def category(request):
    if request.method == 'POST':
        form = category_listform(request.POST, request.FILES)
        if form.is_valid():
            
            data = form.save(commit=False)
            data.UserId=request.user
            data.save()
            return HttpResponseRedirect(reverse('admin_panel:category'))
        else:
            print(form.errors)
    else:
        form = category_listform()
        form = category_listform()
        data = category_list.objects.all()
    return render(request, 'admin_panel/vehical_category.html', {'form': form, 'data' : data})


def updatecategory(request, id):
    details = category_list.objects.get(id=id)
    form_v = category_listform(instance=details)
    if request.method == "POST":
        form_v = category_listform(request.POST, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:category")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/vehical_category.html", {'form' : form_v})


def deletecategory(request, id):
    details = category_list.objects.get(id=id)
    details.delete()
    return redirect("admin_panel:category")





def Add_Vehical_Variant(request):
    if request.method == 'POST':
        form = vehical_Variantform(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.UserId=request.user
            data.save()
            return HttpResponseRedirect(reverse('admin_panel:Vehical_Variant'))
        else:
            print(form.errors)
    else:
        form = vehical_Variantform()
        data = vehical_Variant.objects.all()
    return render(request, 'admin_panel/Add_Variant.html', {'form': form, 'data' : data})



def Vehical_Variant(request):
    form = vehical_Variantform()
    data = vehical_Variant.objects.all()
    return render(request, 'admin_panel/Vehical_Variant.html', { 'data' : data})
    

def updatevariant(request, id):
    details = vehical_Variant.objects.get(id=id)
    form_v = vehical_Variantform(instance=details)
    if request.method == "POST":
        form_v = vehical_Variantform(request.POST, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:Vehical_Variant")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/Add_Variant.html", {'form' : form_v})


def deletevariant(request, id):
    details = vehical_Variant.objects.get(id=id)
    details.delete()
    return redirect("admin_panel:Vehical_Variant")


def vehical_Registration(request):
    if request.method == 'POST':
        form = Vehical_Registrationform(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.UserId=request.user
            data.save()
            return HttpResponseRedirect(reverse('admin_panel:Register_Vehical_List'))
        else:
            print(form.errors)
    else:
        form = Vehical_Registrationform()
        data = Vehical_Registration.objects.all()
    return render(request, 'admin_panel/Vehical_Registration.html', {'form': form, 'data' : data})


def Register_Vehical_List(request):
    form = Vehical_Registrationform()
    data = Vehical_Registration.objects.all()
    return render(request, 'admin_panel/Register_Vehical_List.html', {'data' : data})


def update_Register_Vehical(request, id):
    details = Vehical_Registration.objects.get(id=id)
    form_v = Vehical_Registrationform(instance=details)
    if request.method == "POST":
        form_v = Vehical_Registrationform(request.POST, instance=details)
        if form_v.is_valid():
            user = form_v.save()
            user.save()
            return redirect("admin_panel:Register_Vehical_List")
        else:
            print(form_v.errors)
    return render(request, "admin_panel/Vehical_Registration.html", {'form' : form_v})


def delete_Register_Vehical(request, id):
    details = Vehical_Registration.objects.get(id=id)
    details.delete()
    return redirect("admin_panel:Register_Vehical_List")





def Users(request):
    data = User.objects.all()
    return render(request, 'admin_panel/user_details.html', {'data' : data})

def owner_rq_List(request):
    data = Vehical_Registration.objects.all()
    return render(request, 'admin_panel/owner_Rq_List.html', {'data' : data})