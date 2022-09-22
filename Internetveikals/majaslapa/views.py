from django.shortcuts import render

# Create your views here.
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
    return render(request, 'majaslapa/register.html')

def search(request):
    return render(request, 'majaslapa/search.html')

def contact(request):
    return render(request, 'majaslapa/contact.html')