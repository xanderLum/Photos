# Generated by Django 3.0.3 on 2020-02-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotosAPI', '0004_auto_20200214_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='pubDate',
            field=models.DateTimeField(default='2020-02-17 13:04:28', max_length=11),
        ),
    ]