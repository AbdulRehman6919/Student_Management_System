from django.contrib import admin
from .models import Donor, DonorAmount, Earning, Student,StudentFees,Teacher, TeacherSalary
# Register your models here.
admin.site.register(Student)
admin.site.register(StudentFees)
admin.site.register(Teacher)
admin.site.register(TeacherSalary)
admin.site.register(Donor)
admin.site.register(DonorAmount)
admin.site.register(Earning)
