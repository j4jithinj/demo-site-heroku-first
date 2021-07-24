from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from .forms import *


# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    form = forms.UserForm()
    messages.warning(request, f'Your Profile has been updated!')
    return render(request, 'form.html', {'form': form})

def productview(request):
    products = Product.objects.all()
    return render(request, 'productview.html', {'products':products})

def ProductAdd(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            products = Product.objects.all()
            return render(request, 'productview.html', {'products':products})
    return render(request, 'form.html', {'form':form})


