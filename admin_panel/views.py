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