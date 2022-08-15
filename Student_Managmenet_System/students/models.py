from distutils.command.upload import upload
from sqlite3 import Date
from tkinter import Widget
from typing_extensions import Required
from django.db import models
from datetime import date,datetime
from .widgets import DatePickerInput
from django import forms 
import os 
# Create your models here.

def filepath(request,filename):
    return(os.path.join('uploads/',filename))

class Student (models.Model):

    def fees_left_method(self):
        return self.Total_Addmission_fees-self.discount_price-self.Fees_paid

    def save(self, *args, **kwargs):
        if not self.Fess_left:
            self.Fess_left = self.fees_left_method()
        super(Student, self).save(*args, **kwargs)

    student_id = models.CharField(max_length=50)
    student_birth_num = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admisison_date = models.DateField()
    Guardian_Name = models.CharField(max_length=80)
    Guardian_Address = models.CharField(max_length=200)
    Guardian_Phone_Num_1 = models.IntegerField()
    Guardian_Phone_Num_2 = models.IntegerField(null=True,blank=True)
    Total_Addmission_fees = models.IntegerField(default=2000)
    discount_price = models.IntegerField()
    Fees_paid = models.IntegerField()
    Fess_left = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'images/',null=True,blank=True)

    def __str__(self) -> str:
        return f"Student: {self.first_name} {self.last_name}"


class Teacher (models.Model):

    STATUS_CHOICES = (
    ('current','CURRENT'),
    ('on_leave', 'ON_LEAVE'),
    ('left','LEFT'),
    )

    teacher_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    NID = models.CharField(max_length=80)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='current')
    designation = models.CharField(max_length=150)
    salary = models.IntegerField()
    hired_date = models.DateField(default=date.today().strftime('%Y-%m-%d'))
    image = models.ImageField(upload_to = 'images/',null=True,blank=True)

    def __str__(self) -> str:
        return f"Teacher: {self.first_name} {self.last_name}"


class TeacherSalary (models.Model):
    
    def fees_left_method(self):
        return (self.total_amount+self.bonus_amount)-self.paid_amount

    def save(self, *args, **kwargs):
        if not self.left_amount:
            self.left_amount = self.fees_left_method()
        super(TeacherSalary, self).save(*args, **kwargs)

    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    current_month = models.DateField(default=date.today().strftime('%Y-%m-%d'))
    total_salary = models.IntegerField(default=2000)
    bonus_amount = models.IntegerField(default=0)
    paid_amount = models.IntegerField(default=0)
    left_amount = models.PositiveIntegerField(default=2000)
    date_time_logged = models.DateTimeField(default=datetime.now())





class StudentFees(models.Model):

    def fees_left_method(self):
        return self.total_amount-self.discount_amount-self.paid_amount

    def save(self, *args, **kwargs):
        if not self.left_amount:
            self.left_amount = self.fees_left_method()
        super(StudentFees, self).save(*args, **kwargs)
    
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    current_month = models.DateField(default=date.today().strftime('%Y-%m-%d'))
    total_amount = models.IntegerField(default=2000)
    discount_amount = models.IntegerField(default=0)
    paid_amount = models.IntegerField(default=0)
    left_amount = models.PositiveIntegerField(default=0)
    date_time_logged = models.DateTimeField(default=datetime.now())

# .strftime("%d/%m/%Y %H:%M:%S")