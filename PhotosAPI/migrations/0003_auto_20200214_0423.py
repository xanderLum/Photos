# Generated by Django 3.0.3 on 2020-02-13 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotosAPI', '0002_auto_20200214_0337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='path',
        ),
        migrations.AlterField(
            model_name='photo',
            name='pubDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 4, 23, 18, 387853), max_length=11),
        ),
    ]
