# Generated by Django 3.0.3 on 2020-07-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20200714_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrokedcoursemodel',
            name='cn',
        ),
        migrations.AddField(
            model_name='enrokedcoursemodel',
            name='cn',
            field=models.ManyToManyField(default=0, to='app1.NesclassModel'),
        ),
    ]
