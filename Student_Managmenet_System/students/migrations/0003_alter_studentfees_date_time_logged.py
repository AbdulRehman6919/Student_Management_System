# Generated by Django 3.2.15 on 2022-08-13 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20220813_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentfees',
            name='date_time_logged',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 13, 23, 51, 26, 469848)),
        ),
    ]
