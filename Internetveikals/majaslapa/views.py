from django.shortcuts import render, redirect
from .forms import  CreateUserForm
# from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
# from .models import *
# from .forms import OrderForm, CreateUserForm
# from .filters import OrderFilter

def sakums(request):
    return render(request, 'majaslapa/home.html')

def account(request):
    return render(request, 'majaslapa/account.html')

def about(request):
    return render(request, 'majaslapa/about.html')

def sakums(request):
    return render(request, 'majaslapa/home.html')

def login(request):
    return render(request, 'majaslapa/login.html')

def register(request):
    form = CreateUserForm(request.POST)

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')


    context = {'form': form}
    return render(request, 'majaslapa/register.html', context)

def search(request):
    return render(request, 'majaslapa/search.html')

def contact(request):
    return render(request, 'majaslapa/contact.html')