from turtle import st
from unicodedata import name
from django.shortcuts import render,redirect

import students
from .models import Donor, DonorAmount, Earning, Student,StudentFees,Teacher,TeacherSalary
from .forms import DonorAmountForm, DonorForm, EarningForm, StudentForm,StudentFeesForm, TeacherForm, TeacherSalaryForm

from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

#View All Records Section 

def index(request):
    return render(request, 'students/index.html',{
        'students':Student.objects.all(),
    })

def view_teacher_records(request):
    return render(request,'students/view_teacher_records.html',{
        'teachers':Teacher.objects.all(),
    })

def view_monthly_fees(request):
    return render(request, 'students/view_monthly_fees.html',{
        'students':StudentFees.objects.all(),
    })
def view_monthly_salary(request):
    return render(request, 'students/view_monthly_salary.html',{
        'teachers':TeacherSalary.objects.all(),
    })
def view_donor_amount(request):
    return render(request, 'students/view_donor_amount.html',{
        'donors':DonorAmount.objects.all(),
    })
def view_donor_records(request):
    return render(request,'students/view_donor_records.html',{
        'donors':Donor.objects.all(),
    })
def view_earning_records(request):

    #Amount Calculation
    total_amount = 0
    students = Student.objects.all()
    for i in students:
        total_amount += i.Fees_paid
    
    students_fees = StudentFees.objects.all()
    for i in students_fees:
        total_amount += i.paid_amount

    data = Earning.objects.filter(type ='instituitions')
    if data:
        data_new = Earning.objects.get(type ='instituitions')
        data_new.amount = total_amount
        data_new.save()
    else:
        earning_obj = Earning()
        earning_obj.earning_id=1
        earning_obj.type = 'instituitions'
        earning_obj.description = "Intitutions Amount Sum up"
        earning_obj.amount = total_amount
        earning_obj.save()

    donor_amount= 0 
    donors = DonorAmount.objects.all()
    for i in donors:
        donor_amount += i.amount
    data = Earning.objects.filter(type ='donation')
    if data:
        data_new = Earning.objects.get(type ='donation')
        data_new.amount = donor_amount
        data_new.save()
    else:
        earning_obj = Earning()
        earning_obj.earning_id=2
        earning_obj.type = 'donation'
        earning_obj.description = "Donation Amount Sum up"
        earning_obj.amount = donor_amount
        earning_obj.save()

    return render(request,'students/view_earning_records.html',{
        'earnings':Earning.objects.all(),
    })


#Search Section 

def search_student(request):

    if request.method == "POST":
        searched = request.POST['search_bar']
        serached_students = Student.objects.filter(first_name__contains=searched) or Student.objects.filter(last_name__contains=searched) or Student.objects.filter(Guardian_Phone_Num_1__contains=searched) or Student.objects.filter(Guardian_Phone_Num_2__contains=searched) or Student.objects.filter(Guardian_Name__contains=searched)
        return render(request, 'students/student_fees_search.html',{'searched':searched,'searched_students':serached_students})
    else:
        return render(request, 'students/student_fees_search.html',{})

def search_teacher(request):
    if request.method == "POST":
        searched = request.POST['search_bar']
        serached_teachers = Teacher.objects.filter(first_name__contains=searched) or Teacher.objects.filter(last_name__contains=searched) 
        return render(request, 'students/teacher_salary_search.html',{'searched':searched,'serached_teachers':serached_teachers})
    else:
        return render(request, 'students/teacher_salary_search.html',{})

def search_donor(request):
    if request.method == "POST":
        searched = request.POST['search_bar']
        serached_donors = Donor.objects.filter(donor_name__contains=searched) or Donor.objects.filter(phone_num__contains=searched) 
        return render(request, 'students/donor_amount_search.html',{'searched':searched,'serached_donors':serached_donors})
    else:
        return render(request, 'students/donor_amount_search.html',{})



# Edit Section
def view_student(request,id):
  
    student  = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
def view_teacher(request,id):
  
    teacher  = Teacher.objects.get(pk=id)
    return HttpResponseRedirect(reverse('view_teacher_records'))
def view_donor(request,id):
    donor  = Donor.objects.get(pk=id)
    return HttpResponseRedirect(reverse('view_donor_records'))

def view_earning(request,id):
    earning =  Earning.objects.get(pk=id)
    return HttpResponseRedirect(reverse('view_earning_records'))


# Edit Section

def edit_student(request,id):
    if request.method == 'POST':
        student  = Student.objects.get(pk=id)
        form  = StudentForm(request.POST,request.FILES,instance=student)
        student.Fess_left = str(int(form['Total_Addmission_fees'].value()) - int(form['discount_price'].value())-int(form['Fees_paid'].value()))
     
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_student.html',{'form':form,'success':True})
    else:
        student  = Student.objects.get(pk=id)
        form  = StudentForm(instance=student)
        student.Fess_left = str(int(form['Total_Addmission_fees'].value()) - int(form['discount_price'].value())-int(form['Fees_paid'].value()))
     
        return render(request, 'students/edit_student.html',{'form':form})
def edit_teacher(request,id):
    if request.method == 'POST':
        teacher  = Teacher.objects.get(pk=id)
        form  = TeacherForm(request.POST,request.FILES,instance=teacher)
        
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_teacher.html',{'form':form,'success':True})
    else:
        teacher  = Teacher.objects.get(pk=id)
        form  = TeacherForm(instance=teacher)     
        return render(request, 'students/edit_teacher.html',{'form':form})

def edit_donor(request,id):
    if request.method == 'POST':
        donor  = Donor.objects.get(pk=id)
        form  = DonorForm(request.POST,request.FILES,instance=donor)
        
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_donor.html',{'form':form,'success':True})
    else:
        donor  = Donor.objects.get(pk=id)
        form  = DonorForm(instance=donor)     
        return render(request, 'students/edit_donor.html',{'form':form})

def edit_earning(request,id):
    if request.method == 'POST':
        earning  = Earning.objects.get(pk=id)
        form  = EarningForm(request.POST,request.FILES,instance=earning)
        
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_earning.html',{'form':form,'success':True})
    else:
        earning  = Earning.objects.get(pk=id)
        form  = EarningForm(instance=earning)     
        return render(request, 'students/edit_earning.html',{'form':form})   

def edit_student_fees(request,id):
    if request.method == 'POST':
        student_fees  = StudentFees.objects.get(pk=id)
        
        form  = StudentFeesForm(request.POST,request.FILES,instance=student_fees)
        student_fees.left_amount = str(int(form['total_amount'].value()) - int(form['discount_amount'].value())-int(form['paid_amount'].value()))
       
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_student_fees.html',{'form':form,'success':True})
    else:
        student_fees  = StudentFees.objects.get(pk=id)
        form  = StudentFeesForm(instance=student_fees)
        student_fees.left_amount = str(int(form['total_amount'].value()) - int(form['discount_amount'].value())-int(form['paid_amount'].value()))
     
        return render(request, 'students/edit_student_fees.html',{'form':form})

def edit_teacher_salary(request,id):
    if request.method == 'POST':
        teacher_salary  = TeacherSalary.objects.get(pk=id)
        
        form  = TeacherSalaryForm(request.POST,request.FILES,instance=teacher_salary)
        teacher_salary.left_amount = str((int(form['total_salary'].value()) + int(form['bonus_amount'].value()))-int(form['paid_amount'].value()))
       
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_teacher_salary.html',{'form':form,'success':True})
    else:
        teacher_salary  = TeacherSalary.objects.get(pk=id)
        form  = TeacherSalaryForm(instance=teacher_salary)
        teacher_salary.left_amount = str((int(form['total_salary'].value()) + int(form['bonus_amount'].value()))-int(form['paid_amount'].value()))
     
        return render(request, 'students/edit_teacher_salary.html',{'form':form})

def edit_donor_amount(request,id):
    if request.method == 'POST':
        donor_amount  = DonorAmount.objects.get(pk=id) 
        form  = DonorAmountForm(request.POST,request.FILES,instance=donor_amount)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_donor_amount.html',{'form':form,'success':True})
    else:
        donor_amount  = DonorAmount.objects.get(pk=id)
        form  = DonorAmountForm(instance=donor_amount)
        return render(request, 'students/edit_donor_amount.html',{'form':form})

#Delete Section

def delete_student(request,id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
def delete_teacher(request,id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=id)
        teacher.delete()
    return HttpResponseRedirect(reverse('view_teacher_records'))

def delete_earning(request,id):
    if request.method == "POST":
        earning = Earning.objects.get(pk=id)
        earning.delete()
    return HttpResponseRedirect(reverse('view_earning_records'))

def delete_donor(request,id):
    if request.method == 'POST':
        donor = Donor.objects.get(pk=id)
        donor.delete()
    return HttpResponseRedirect(reverse('view_donor_records'))

def delete_student_fees(request,id):
    if request.method == 'POST':
        student_fees = StudentFees.objects.get(pk=id)
        student_fees.delete()
    return HttpResponseRedirect(reverse('view-monthly-fees'))

def delete_teacher_salary(request,id):
    if request.method == 'POST':
        teacher_salary = TeacherSalary.objects.get(pk=id)
        teacher_salary.delete()
    return HttpResponseRedirect(reverse('view_monthly_salary'))

def delete_donor_amount(request,id):
    if request.method == 'POST':
        donor_amount = DonorAmount.objects.get(pk=id)
        donor_amount.delete()
    return HttpResponseRedirect(reverse('view_donor_amount'))


#Add Section

def add_student_fees(request,id):
    if request.method  == 'POST':
        form  = StudentFeesForm(request.POST)
        

        student_instanace = Student.objects.get(pk=id)
        new_student = StudentFees(
            student_id=student_instanace
            )

        new_student.save()
        return redirect(edit_student_fees,id=new_student.id)
        # return render(request, 'students/student_fees_search.html',{'form':StudentFeesForm(),'success':True})

    else:

        form = StudentFeesForm()
        return render(request,'students/student_fees_search.html',{'form':StudentFeesForm()})

def add_donor_amount(request,id):
    if request.method  == 'POST':
        form  = DonorAmountForm(request.POST)
        

        donor_instanace = Donor.objects.get(pk=id)
        new_donor = DonorAmount(
            donor_id=donor_instanace
            )

        new_donor.save()
        return redirect(edit_donor_amount,id=new_donor.id)

    else:

        form = DonorAmountForm()
        return render(request,'students/donor_amount_search.html',{'form':DonorAmountForm()})    

def add_teacher_salary(request,id):
    if request.method  == 'POST':
        form  = TeacherSalaryForm(request.POST)
        

        teacher_instanace = Teacher.objects.get(pk=id)
        new_teacher = TeacherSalary(
            teacher_id=teacher_instanace
            )

        new_teacher.save()
        return redirect(edit_teacher_salary,id=new_teacher.id)

    else:

        form = TeacherSalaryForm()
        return render(request,'students/teacher_salary_search.html',{'form':TeacherSalaryForm()})

def add_teacher(request):
    if request.method  == 'POST':
        
        form  = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            
            new_teacher_id=form.cleaned_data['teacher_id']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_NID=form.cleaned_data['NID']
            new_status = form.cleaned_data['status']
            new_designation = form.cleaned_data['designation']
            new_salary = form.cleaned_data['salary']
            new_image = form.cleaned_data['image']
            new_hired_date = form.cleaned_data['hired_date']


            new_teacher = Teacher(
                teacher_id=new_teacher_id,
                first_name =new_first_name ,
                last_name = new_last_name ,
                NID =new_NID,
                status =new_status,
                designation =new_designation,
                image  = new_image,
                salary = new_salary,
                hired_date=new_hired_date
                )

            new_teacher.save()

            return render(request, 'students/add_teacher.html',{'form':TeacherForm(),'success':True})

    else:

        form = TeacherForm()
        return render(request,'students/add_teacher.html',{'form':TeacherForm()})

def add_donor(request):
    if request.method  == 'POST':
        
        form  = DonorForm(request.POST,request.FILES)
        if form.is_valid():
            
            new_donor_id=form.cleaned_data['donor_id']
            new_name = form.cleaned_data['donor_name']
            new_NID=form.cleaned_data['NID']
            new_phone_num = form.cleaned_data['phone_num']
            new_image = form.cleaned_data['image']
        


            new_donor = Donor(
                donor_id=new_donor_id,
                donor_name =new_name ,
                NID =new_NID,
                phone_num = new_phone_num,
                image  = new_image,
            
                )

            new_donor.save()

            return render(request, 'students/add_donor.html',{'form':DonorForm(),'success':True})

    else:

        form = DonorForm()
        return render(request,'students/add_donor.html',{'form':DonorForm()})

def add_earning (request):
    if request.method  == 'POST':
        
        form  = EarningForm(request.POST,request.FILES)
        if form.is_valid():
            
            new_earning_id=form.cleaned_data['earning_id']
            new_description = form.cleaned_data['description']
            new_amount = form.cleaned_data['amount']
            new_type = form.cleaned_data['type']
            new_comment = form.cleaned_data['comment']

            new_earning = Earning(
                earning_id=new_earning_id,
                description =new_description ,
                amount = new_amount ,
                type = new_type,
                comment = new_comment
                )

            new_earning.save()

            return render(request, 'students/add_earning.html',{'form':EarningForm(),'success':True})

    else:

        form = EarningForm()
        return render(request,'students/add_earning.html',{'form':EarningForm()})



def add_student(request):
    if request.method  == 'POST':
        
        form  = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            
            new_student_id=form.cleaned_data['student_id']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_admisison_date=form.cleaned_data['admisison_date']
            new_Guardian_Name = form.cleaned_data['Guardian_Name']
            new_Guardian_Address = form.cleaned_data['Guardian_Address']
            new_Guardian_Phone_Num_1 = form.cleaned_data['Guardian_Phone_Num_1']
            new_Guardian_Phone_Num_2 = form.cleaned_data['Guardian_Phone_Num_2']
            new_Total_Addmission_fees = form.cleaned_data['Total_Addmission_fees']
            new_discount_price = form.cleaned_data['discount_price']
            new_Fees_paid = form.cleaned_data['Fees_paid']
            new_image = form.cleaned_data['image']
            new_birth_card_num = form.cleaned_data['student_birth_num']

            new_student = Student(
                student_id=new_student_id,
                first_name =new_first_name ,
                last_name = new_last_name ,
                admisison_date =new_admisison_date,
                Guardian_Name =new_Guardian_Name,
                Guardian_Address =new_Guardian_Address,
                Guardian_Phone_Num_1 = new_Guardian_Phone_Num_1,
                Guardian_Phone_Num_2 =new_Guardian_Phone_Num_2,
                Total_Addmission_fees = new_Total_Addmission_fees,
                discount_price = new_discount_price,
                Fees_paid = new_Fees_paid,
                image  = new_image,
                student_birth_num  = new_birth_card_num
                )

            new_student.save()

            return render(request, 'students/add_student.html',{'form':StudentForm(),'success':True})

    else:

        form = StudentForm()
        return render(request,'students/add_student.html',{'form':StudentForm()})


 