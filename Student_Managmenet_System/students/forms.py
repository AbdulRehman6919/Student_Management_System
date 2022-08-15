from socket import fromshare
from tkinter import Widget
from .models import Student,StudentFees,Teacher,TeacherSalary
from django import forms 
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput


class DateInput(forms.DateInput):
    input_type = 'date'


class TeacherSalaryForm(forms.ModelForm):
    class Meta:
        model = TeacherSalary
        fields = ['teacher_id','current_month','total_salary','bonus_amount','paid_amount']
                # fields = '__all__'  you can also add that line to include all fields in that form 

        labels ={
            'teacher_id': 'Teacher ID',
            'current_month': 'Cuurent Month',
            'total_salary' : 'Total Salary ',
            'bonus_amount': 'Bonus Amount',
            'paid_amount': 'Paid Amount',
            
        }

        widgets = {
            'teacher_id': forms.NumberInput(attrs={'class':'form-control'}),
            'total_salary' : forms.NumberInput(attrs={'class':'form-control'}),
            'bonus_amount' : forms.NumberInput(attrs={'class':'form-control'}),
            'paid_amount' : forms.NumberInput(attrs={'class':'form-control'}),
            'current_month':DateInput() ,
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_id','NID','first_name','last_name','hired_date','status','designation','salary','image']
        # fields = '__all__'  you can also add that line to include all fields in that form 
        # admission_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
        labels ={
            'teacher_id': 'Teacher ID',
            'NID' : 'ID No.',
            'first_name': 'First Name',
            'last_name' : 'Last Name',
            'hired_date':'Hired Date',
            'status': 'Status',
            'designation': 'Designation',
            'salary': 'Salary',
            'image': 'Image'
        }

        widgets = {
        
            'teacher_id': forms.NumberInput(attrs={'class':'form-control'}),
            'NID':forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Taka'}),
            'hired_date':DateInput()
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','student_birth_num','first_name','last_name','admisison_date','Guardian_Name','Guardian_Address','Guardian_Phone_Num_1',
        'Guardian_Phone_Num_2','Total_Addmission_fees','discount_price','Fees_paid','image']
        # fields = '__all__'  you can also add that line to include all fields in that form 
        # admission_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
        labels ={
            'student_id': 'Student ID',
            'StudentImage' : 'Upload Image',
            'first_name': 'First Name',
            'last_name' : 'Last Name',
            'admisison_date': 'Admission Date',
            'Guardian_Name': 'Guardian Name',
            'Guardian_Address': 'Guardian Address',
            'Guardian_Phone_Num_1': 'Guardian Phone (NUM 1)',
            'Guardian_Phone_Num_2': 'Guardian Phone (NUM 2)',
            'Total_Addmission_fees': 'Total Addmission Fee',
            'discount_price' : 'Discount Price',
            'Fees_paid': 'Fees Paid',
            'image':"Image",
            'student_birth_num':'Student Birth Number'
        }

        widgets = {
            # 'student_id': forms.NumberInput(attrs={'class':'form-control','placeholder': '1'}),
            'student_id': forms.NumberInput(attrs={'class':'form-control'}),
            'student_birth_num':forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'admisison_date':DateInput() ,
            'Guardian_Name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Father | Mother | CareTaker'}),
            'Guardian_Address': forms.TextInput(attrs={'class':'form-control'}),
            'Guardian_Phone_Num_1': forms.NumberInput(attrs={'class':'form-control','placeholder': 'XXXXXXXXXXX'}),
            'Guardian_Phone_Num_2': forms.NumberInput(attrs={'class':'form-control','placeholder': 'XXXXXXXXXXX'}),
            'Total_Addmission_fees': forms.NumberInput(attrs={'class':'form-control'}),
            'discount_price' : forms.NumberInput(attrs={'class':'form-control'}),
            'Fees_paid': forms.NumberInput(attrs={'class':'form-control'}),
          
        
        }

class StudentFeesForm(forms.ModelForm):
    class Meta:
        model = StudentFees
        fields = ['student_id','current_month','total_amount','discount_amount','paid_amount']
        # fields = '__all__'  you can also add that line to include all fields in that form 

        labels ={
            'student_id': 'Student ID',
            'current_month': 'Cuurent Month',
            'total_amount' : 'Total Amount ',
            'discount_amount': 'Discount Amount',
            'paid_amount': 'Paid Amount',
            
        }

        widgets = {
            'student_id': forms.NumberInput(attrs={'class':'form-control'}),
            'total_amount' : forms.NumberInput(attrs={'class':'form-control'}),
            'discount_amount' : forms.NumberInput(attrs={'class':'form-control'}),
            'paid_amount' : forms.NumberInput(attrs={'class':'form-control'}),
            'current_month':DateInput() ,
        }
