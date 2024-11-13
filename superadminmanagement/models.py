from django.db import models
import random
import datetime
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

currentdatetime = datetime.datetime.now()

generate_id = currentdatetime.strftime("%f")



# Generating Random Number
random_number = random.randint(5, 9999)

# Students Information
class StudentInfo(models.Model):
    student_id = models.CharField(max_length=10, default="MGSD"+generate_id,  unique=True, verbose_name="Student ID -Genereated")
    firstname = models.CharField(max_length=20, verbose_name="First Name")
    lastname = models.CharField(max_length=20, verbose_name="Last Name")
    fathername = models.CharField(max_length=20, verbose_name="Father's Name")
    mothername = models.CharField(max_length=20, verbose_name="Mother's Name")
    address = models.TextField(default="", verbose_name="Permanent Address")
    guardian_phone = models.CharField(max_length=20, verbose_name="Guardian Phone Number")
    student_phone = models.CharField(max_length=20, verbose_name="Student Phone Number")
    student_email = models.EmailField(max_length=40, verbose_name="Email Address (If any)", blank=True)
    profile_image = models.ImageField(upload_to="students/", null=True, blank=True)

    def __str__(self):
        return self.student_id+" "+self.firstname
    

# Teachers Information
class TeacherInfo(models.Model):
    teacher_id = models.CharField(max_length=8, default="TCHR"+str(random_number), verbose_name="Teacher ID (Generated)", unique=True)
    firstname = models.CharField(max_length=20, verbose_name="First Name")
    lastname = models.CharField(max_length=20, verbose_name="Last Name")
    teacher_of_subject = models.CharField(max_length=30, verbose_name="Dedicated Subject")
    last_graduated_degree = models.CharField(max_length=30, verbose_name="Last Graduation Degree")
    last_graduated_subject = models.CharField(max_length=30, verbose_name="Subject of Graduation")
    last_graduated_university = models.CharField(max_length=30, verbose_name="Graduated from University")
    last_graduated_session = models.CharField(max_length=30, verbose_name="Session")
    address = models.TextField(default="", verbose_name="Permanent Address")
    teacher_phone = models.CharField(max_length=20, verbose_name="Phone Number")
    teacher_email = models.EmailField(max_length=40, verbose_name="Email Address")
    profile_image = models.ImageField(upload_to="teachers/", null=True, blank=True)

    def __str__(self):
        return self.firstname+" - "+self.teacher_of_subject



# Staff Information
class StaffInfo(models.Model):
    staff_id = models.CharField(max_length=8, default="STFF"+str(random_number), verbose_name="Staff ID (Generated)", unique=True)
    staff_firstname = models.CharField(max_length=20, verbose_name="First Name")
    staff_lastname = models.CharField(max_length=20, verbose_name="Last Name")
    edu_qualification = models.CharField(max_length=30, verbose_name="Educational Qualification" ,null=True)
    staff_job_department = models.CharField(max_length=30, verbose_name="Staff Department")
    address = models.TextField(default="", verbose_name="Permanent Address")
    staff_phone = models.CharField(max_length=20, verbose_name="Phone Number")
    staff_email = models.EmailField(max_length=40, blank=True, verbose_name="Email Address")
    staff_image = models.ImageField(upload_to="staffs/", null=True, blank=True)
    

    def __str__(self):
        return self.staff_firstname+" - "+self.staff_job_department
    

# ACADEMIC NOTICE FOR ALL CATEGORIES #

class Notice(models.Model):

    category_choice = {
        ('1', 'All'),
        ('2', 'Students'),
        ('3', 'Teachers'),
        ('4', 'Staffs'),
        ('5', 'Students & Teachers'),
        ('6', 'Staffs & Teachers'),
        ('7', 'Administrations'),
    }

    ACTION_CHOICE = {
        ('1', 'Publish'),
        ('0', 'Save as Draft'),
    }

    notice_subject  = models.CharField(max_length=255)
    notice_body     = RichTextField()
    publish_date    = models.DateTimeField(auto_now_add=True)
    publish_category = models.CharField(max_length=20, choices=category_choice, default=1)
    active_status   = models.CharField(max_length=2, choices=ACTION_CHOICE, default=1)


    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.notice_subject