# Generated by Django 3.0.3 on 2020-07-14 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_enrokedcoursemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrokedcoursemodel',
            name='cn',
        ),
        migrations.AddField(
            model_name='enrokedcoursemodel',
            name='cn',
            field=models.ManyToManyField(to='app1.NesclassModel'),
        ),
    ]