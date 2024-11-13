from django.urls import path 
from . import views


app_name = 'auth'

urlpatterns = [
    path('', views.loginview, name='login'),
    path('signup', views.SignUpView, name='signup'),
]