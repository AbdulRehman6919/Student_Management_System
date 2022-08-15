from django.contrib import admin
from .models import Student,StudentFees,Teacher, TeacherSalary
# Register your models here.
admin.site.register(Student)
admin.site.register(StudentFees)
admin.site.register(Teacher)
admin.site.register(TeacherSalary)