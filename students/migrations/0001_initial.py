# Generated by Django 3.2.15 on 2022-08-13 17:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=50)),
                ('student_birth_num', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('admisison_date', models.DateField()),
                ('Guardian_Name', models.CharField(max_length=80)),
                ('Guardian_Address', models.CharField(max_length=200)),
                ('Guardian_Phone_Num_1', models.IntegerField()),
                ('Guardian_Phone_Num_2', models.IntegerField(blank=True, null=True)),
                ('Total_Addmission_fees', models.IntegerField(default=2000)),
                ('discount_price', models.IntegerField()),
                ('Fees_paid', models.IntegerField()),
                ('Fess_left', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_month', models.DateField(default='2022-08-13')),
                ('total_amount', models.IntegerField(default=2000)),
                ('discount_amount', models.IntegerField(default=0)),
                ('paid_amount', models.IntegerField(default=0)),
                ('left_amount', models.PositiveIntegerField(default=0)),
                ('date_time_logged', models.DateTimeField(default=datetime.datetime(2022, 8, 13, 22, 0, 20, 234941))),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]
