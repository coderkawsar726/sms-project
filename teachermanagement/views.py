from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from assignment.models import Assignment, BookList
from .forms import AddAssignForm, CompleteAssForm
from django.urls import reverse_lazy

# Teacher Index Page 
def Index(request):
    context = {
        'pagetitle': 'Teacher Panel',
        'paneltitle': 'Dashboard',
    }
    return render(request, 'teacher/index.html', context)



# Teacher Take Attendance
def TakeAttendance(request):
    context = {
        'pagetitle': 'Take Attendance',
        'paneltitle': 'Particular Class Attendances',
    }
    return render(request, 'teacher/takeattendance.html', context)


# Teacher Accept or Declient a Leave
def AproveLeave(request):
    assignment = Assignment.objects.all()
    context = {
        'pagetitle': 'Leave Aproval',
        'paneltitle': 'Aprove student pending leaves',
        'data': assignment,
    }
    return render(request, 'teacher/aproveleave.html', context)



# Show Subject of Each Classes for assignment
def Assignments(request):
    class_one = BookList.objects.filter(classfor=1)
    class_two = BookList.objects.filter(classfor=2)
    class_three = BookList.objects.filter(classfor=3)
    class_four = BookList.objects.filter(classfor=4)
    class_five = BookList.objects.filter(classfor=5)
    assignment = Assignment.objects.all()
    context = {
        'assignment': assignment,
        'pagetitle': 'Assignments & Homework',
        'paneltitle': 'Homework / Assignment Integrations',
        'class_one': class_one,
        'class_two': class_two,
        'class_three': class_three,
        'class_four': class_four,
        'class_five': class_five,

    }
    return render(request, 'teacher/assignment.html', context)




# Assignment Submission Form
def AddAssignment(request, sb, cl):
    initialdata = {
        'subject': sb,
        'stclass': cl,
    }
    form = AddAssignForm(initial=initialdata)
    if request.method == 'POST':
        form = AddAssignForm(request.POST, initial=initialdata)
        if form.is_valid():
            form.save()
            return redirect('teacher:assignlist', subcode=sb, st_class=cl)
            
    context = {
        'form':form,
        'subject':sb,
        'stclass': cl,
    }
    return render(request, 'teacher/addassignment.html', context)



# Retrive Assignments Data for each classes
def AssignList(request, subcode, st_class):

    assign = Assignment.objects.filter(stclass=st_class, subject=subcode, activation=1)
    context = {
        'assign': assign,
        'subject':subcode,
        'class': st_class,
    }
    return render(request, 'teacher/assignlist.html', context)




# To show individual Assignment
class ShowAssignment(DetailView):
    model = Assignment
    template_name = 'teacher/assignmentdetails.html'



# Configuring assingment which is shown or not
def DeleteAssignment(request, pk):
    instancedata = Assignment.objects.get(pk=pk)
   
    form = AddAssignForm(instance=instancedata)
    if request.method == 'POST':
        form = AddAssignForm(request.POST, instance=instancedata)
        if form.is_valid():
            form.save(commit=False)
            instancedata.activation = '0'
            form.save()
            return redirect('teacher:assignlist', subcode=instancedata.subject.id, st_class=instancedata.stclass)
            
    context = {
        'form':form,
        'subject': instancedata.subject,
        'stclass': instancedata.stclass,
    }
    return render(request, 'teacher/deleteassignment.html', context)
