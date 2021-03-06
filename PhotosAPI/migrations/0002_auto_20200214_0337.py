# Generated by Django 3.0.3 on 2020-02-13 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotosAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='imageFile',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='pubDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 3, 37, 33, 789031), max_length=11),
        ),
        migrations.AlterField(
            model_name='photo',
            name='status',
            field=models.CharField(default='P', max_length=1),
        ),
    ]
