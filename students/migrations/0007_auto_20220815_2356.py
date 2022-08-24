# Generated by Django 3.2.15 on 2022-08-15 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20220814_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_id', models.IntegerField()),
                ('NID', models.CharField(blank=True, max_length=80, null=True)),
                ('donor_name', models.CharField(max_length=200)),
                ('phone_num', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='studentfees',
            name='current_month',
            field=models.DateField(default='2022-08-15'),
        ),
        migrations.AlterField(
            model_name='studentfees',
            name='date_time_logged',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 23, 56, 11, 174603)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='hired_date',
            field=models.DateField(default='2022-08-15'),
        ),
        migrations.AlterField(
            model_name='teachersalary',
            name='current_month',
            field=models.DateField(default='2022-08-15'),
        ),
        migrations.AlterField(
            model_name='teachersalary',
            name='date_time_logged',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 23, 56, 11, 174603)),
        ),
    ]
