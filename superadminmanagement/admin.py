from django.contrib import admin
from .models import StudentInfo, TeacherInfo, StaffInfo

# Register your models here.

# admin.site.register(TestAssignment)
admin.site.register(StudentInfo)
admin.site.register(TeacherInfo)
admin.site.register(StaffInfo)
