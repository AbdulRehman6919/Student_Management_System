# Generated by Django 3.2.15 on 2022-08-17 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20220817_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donoramount',
            name='date',
            field=models.DateField(default='2022-08-17'),
        ),
        migrations.AlterField(
            model_name='donoramount',
            name='date_time_logged',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 23, 39, 6, 916953), null=True),
        ),
        migrations.AlterField(
            model_name='studentfees',
            name='date_time_logged',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 23, 39, 6, 915976)),
        ),
        migrations.AlterField(
            model_name='teachersalary',
            name='date_time_logged',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 23, 39, 6, 915000)),
        ),
    ]
