from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:id>',views.view_student,name= 'view_student'),
    path('add_student',views.add_student,name = 'add_student'),
    path('edit_student/<int:id>/',views.edit_student,name = 'edit_student'),
    path('delete_student/<int:id>/',views.delete_student,name='delete_student'),
    path('search_student',views.search_student,name ='search-student'),
    path('view_monthly_fees', views.view_monthly_fees,name='view-monthly-fees'),
    path('add_student/<int:id>/', views.add_student_fees,name='add_student_fees'),
    path('delete_student_fees/<int:id>/',views.delete_student_fees,name='delete-student-fees'),
    path('edit_student_fees/<int:id>/',views.edit_student_fees,name= 'edit_student_fees'),


    path('view_teacher_records',views.view_teacher_records,name ='view_teacher_records'),
    path('add_teacher',views.add_teacher,name= 'add_teacher'),
    path('edit_teacher/<int:id>/',views.edit_teacher,name = 'edit_teacher'),
    path('delete_teacher/<int:id>/',views.delete_teacher,name = 'delete_teacher'),
    path('view_teacher/<int:id>',views.view_teacher,name= 'view_teacher'),

    path('delete_teacher_salary/<int:id>/',views.delete_teacher_salary,name='delete_teacher_salary'),
    path('edit_teacher_salary/<int:id>/',views.edit_teacher_salary,name= 'edit_teacher_salary'),
    path('view_monthly_salary', views.view_monthly_salary,name='view_monthly_salary'),
    path('search_teacher',views.search_teacher,name ='search_teacher'),
    path('add_teacher_salary/<int:id>/', views.add_teacher_salary,name='add_teacher_salary'),
]