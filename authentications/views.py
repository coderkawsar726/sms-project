from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def loginview(request):
    context = {
        'pagetitle': 'User Login',
    }
    return render(request, 'auth/signin.html', context)

def SignUpView(request):
    context = {
        'pagetitle': 'SignUp Page',
    }
    return render(request, 'auth/registration.html', context)
