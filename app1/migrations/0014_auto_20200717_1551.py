# Generated by Django 3.0.3 on 2020-07-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_auto_20200717_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrokedcoursemodel',
            name='cn',
        ),
        migrations.AddField(
            model_name='enrokedcoursemodel',
            name='cn',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='enrokedcoursemodel',
            name='sid',
        ),
        migrations.AddField(
            model_name='enrokedcoursemodel',
            name='sid',
            field=models.IntegerField(default=0),
        ),
    ]