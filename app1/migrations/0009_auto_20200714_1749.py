# Generated by Django 3.0.3 on 2020-07-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20200714_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nesclassmodel',
            name='cid',
            field=models.IntegerField(default=0),
        ),
    ]
