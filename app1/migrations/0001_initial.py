# Generated by Django 3.0.3 on 2020-07-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NesclassModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=49)),
                ('faculty', models.CharField(max_length=49)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('fee', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]