from django.urls import path 
from . import views


app_name = 'superadmin'

urlpatterns = [
    path('', views.Dashboard, name="admindashboard"),
    path('booklist/', views.Booklist.as_view(), name="booklist"),
    path('addbook/', views.AddBook.as_view(), name="addbook"),
    path('<pk>/updatebook', views.UpdateBook.as_view(), name="updatebook"),
    path('<pk>/delete/', views.DeleteBook.as_view(), name="deletebook"),
    path('addstudent/', views.AddStudent.as_view(), name="addstudent"),
    path('students/', views.AllStudent.as_view(), name="allstudent"),
    path('studentdetail/<pk>', views.StudentDetail.as_view(), name="studentdetail"),
    path('createnotice/', views.CreateNotice.as_view(), name="createnotice"),
    path('noticelist/', views.ListNotice, name="noticelist"),
    path('readnotice/<pk>', views.ReadNotice.as_view(), name="readnotice"),
    path('updatenotice/<pk>', views.UpdateNotice.as_view(), name="updatenotice"),
    path('deletenotice/<pk>', views.DeleteNotice.as_view(), name="deletenotice"),
]