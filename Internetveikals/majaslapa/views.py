from django.shortcuts import render, redirect
from .forms import  CreateUserForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# from majaslapa.register_login.utils import send_email_for_verify

from django.contrib.auth import get_user_model


User = get_user_model()

# Create your views here.
def sakums(request):
    return render(request, 'majaslapa/home.html')

def account(request):
    return render(request, 'majaslapa/account.html')

def about(request):
    return render(request, 'majaslapa/about.html')

def sakums(request):
    return render(request, 'majaslapa/home.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('sakums')
        else:
            messages.info(request, 'Nav pareizs lietotājvārds vai parole')

    context = {}
    return render(request, 'majaslapa/login.html', context)

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

def logoutUser(request):
    logout(request)
    return redirect('login')