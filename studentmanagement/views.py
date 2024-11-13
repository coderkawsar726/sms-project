from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from assignment.models import Assignment
from superadminmanagement.models import Notice


def StudentDashboard(request):
    context = {
        'pagetitle': 'Student Dashboard',
        'paneltitle': 'Dashboard Panel',
        'active_st_dashboard': True,
    }
    return render(request, 'student/dashboard.html', context)

def StudentProfile(request):
    context = {
        'pagetitle': 'Student Profile',
        'paneltitle': 'My Profile Panel',
        'active_st_profile': True,
    }
    return render(request, 'student/myprofile.html', context)

def StudentShowAttendance(request):
    context = {
        'pagetitle': 'Attendance Record',
        'paneltitle': 'Show Attendance Report',
        'active_st_attendance': True,
    }
    return render(request, 'student/attendance.html', context)




def StudentAssignment(request):
    assignments = Assignment.objects.filter(stclass=1, activation=1)
    context = {
        'pagetitle': 'View Class Assignment',
        'paneltitle': 'Class Assignment By Teachers',
        'active_st_assignment': True,
        'assignments': assignments,
    }
    return render(request, 'student/assignment.html', context)




def PrintAssignment(request):
    assignment = Assignment.objects.filter(stclass=1, activation=1)
    context = {
        'assignment': assignment,
    }
    return render(request, 'student/assignprint.html', context)



def StudentPayment(request):
    context = {
        'pagetitle': 'Payment Option',
        'paneltitle': 'Course fee payment panel',
        'active_st_payment': True,
    }
    return render(request, 'student/payment.html', context)

class StudentNotice(ListView):
    model = Notice
    template_name = 'student/noticeboard.html'
    context_object_name = 'notice'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['mynotice'] = Notice.objects.filter(publish_category=1)
        context['pagetitle'] = 'Announcement for Students'
        context['paneltitle'] = 'Announcement panel for students'
        context['active_st_notice'] = True

        return context

def StudentLeave(request):
    context = {
        'pagetitle': 'Leave of Absent',
        'paneltitle': 'Student Leave Panel',
        'active_st_leave': True,
    }
    return render(request, 'student/leave.html', context)

