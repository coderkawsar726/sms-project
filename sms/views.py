from django.shortcuts import render

def Index(request):
    active = True
    context = {
        'pagetitle': 'Home | School Management System',
        'home_active': active,
    }
    return render(request, 'auth/home.html', context)