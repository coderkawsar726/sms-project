from django.urls import path 
from . import views


app_name = 'teacher'

urlpatterns = [
    path('', views.Index, name="teacherpanel"),
    path('takeattendance/', views.TakeAttendance, name="takeattendance"),
    path('aproveleave/', views.AproveLeave, name="aproveleave"),
    path('assignment/', views.Assignments, name="assignment"),
    path('assignlist/<int:subcode>/<int:st_class>/', views.AssignList, name="assignlist"),
    path('addassignment/<int:sb>/<int:cl>/', views.AddAssignment, name="addassignment"),
    path('deleteassign/<pk>/', views.DeleteAssignment, name="deleteassign"),
    path('assigndetail/<pk>', views.ShowAssignment.as_view(), name="assigndetail"),
]