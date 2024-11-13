from django.shortcuts import render
import random
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, DetailView
from assignment.models import BookList
from superadminmanagement.models import StudentInfo, TeacherInfo, StaffInfo, Notice
import datetime


# Generate unique id with current date #

currentdatetime = datetime.datetime.now()
generate_id = currentdatetime.strftime("%f")

# -------------------------------------------------------------------- #
# Admin Dashboard View 
def Dashboard(request):
    totalstudent = StudentInfo.objects.count()
    totalteacher = TeacherInfo.objects.count()
    totalstaff = StaffInfo.objects.count()
    context = {
        'totalstudent': totalstudent,
        'totalteacher': totalteacher,
        'totalstaff': totalstaff,
    }
    return render(request, 'superadmin/dashboard.html', context) 



# Create your views here.
class Booklist(ListView):
    model = BookList
    template_name = 'superadmin/academic/booklist.html'
    context_object_name = 'list'

class AddBook(CreateView):
    model = BookList
    fields = "__all__"
    template_name = 'superadmin/academic/addbook.html'
    success_url = reverse_lazy('superadmin:booklist')
    
class UpdateBook(UpdateView):
    model = BookList
    template_name = 'superadmin/academic/update.html'
    success_url = reverse_lazy('superadmin:booklist')
    fields = "__all__"
    
class DeleteBook(DeleteView):
    model = BookList
    template_name = 'superadmin/academic/delete.html'
    success_url = reverse_lazy('superadmin:booklist')


# STUDENT FUNCTIONALITY SECTION #

class AddStudent(CreateView):
    model = StudentInfo
    fields = "__all__"
    template_name = 'superadmin/student/addstudent.html'
    success_url = reverse_lazy('superadmin:admindashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generate_id'] = generate_id
        return context
    
    def get_success_url(self) -> str:
        return reverse_lazy('superadmin:studentdetail', kwargs={'pk': self.object.pk})
    

class AllStudent(ListView):
    model = StudentInfo
    template_name = 'superadmin/student/allStudent.html'
    context_object_name = 'allstudent'

    # Count Total Human
    totalstudent = StudentInfo.objects.count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['totalstudent'] = self.totalstudent

        return context


class StudentDetail(DetailView):
    model = StudentInfo
    template_name = 'superadmin/student/detail.html'
    context_object_name = 'data'



# Notice Functionality #
class CreateNotice(CreateView):
    model = Notice
    fields = "__all__"
    template_name = 'superadmin/academic/addNotice.html'

    def get_success_url(self) -> str:
        return reverse_lazy('superadmin:readnotice', kwargs={'pk': self.object.pk})
    
def ListNotice(request):
    notice = Notice.objects.all() 
    published = Notice.objects.filter(active_status=1)
    draft = Notice.objects.filter(active_status=0)
    
    context = {
       'notice': notice,
       'published': published,
       'draft': draft,
    }
    return render(request, 'superadmin/academic/notices.html', context)


class UpdateNotice(UpdateView):
    model = Notice 
    fields = "__all__"
    template_name = 'superadmin/academic/addNotice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publish'] = True
        return context
    

    def get_success_url(self) -> str:
        return reverse_lazy('superadmin:readnotice', kwargs={'pk': self.object.pk})

class ReadNotice(DetailView):
    model = Notice
    template_name = 'superadmin/academic/individualnotice.html'
    context_object_name = 'notice'

class DeleteNotice(DeleteView):
    model = Notice
    template_name = 'superadmin/academic/delete.html'

    def get_success_url(self) -> str:
        return reverse_lazy('superadmin:noticelist')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back'] = ReadNotice()

        return context
    