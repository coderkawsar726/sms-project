from django.urls import path 
from . import views


app_name = 'student'

urlpatterns = [
    path('', views.StudentDashboard, name="StDashboard"),
    path('myprofile/', views.StudentProfile, name="StProfile"),
    path('showattendance/', views.StudentShowAttendance, name="StShowAttendance"),
    path('showassignment/', views.StudentAssignment, name="StShowAssignment"),
    path('stpayment/', views.StudentPayment, name="StPayment"),
    path('stnotice/', views.StudentNotice.as_view(), name="StNotice"),
    path('stleave/', views.StudentLeave, name="StLeave"),
    path('printassign/', views.PrintAssignment, name="printassign"),
]