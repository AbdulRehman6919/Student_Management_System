# Generated by Django 3.2.15 on 2022-08-17 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20220817_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donoramount',
            name='date_time_logged',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 22, 42, 1, 727953), null=True),
        ),
        migrations.AlterField(
            model_name='studentfees',
            name='date_time_logged',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 22, 42, 1, 726977)),
        ),
        migrations.AlterField(
            model_name='teachersalary',
            name='date_time_logged',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 22, 42, 1, 726977)),
        ),
    ]
