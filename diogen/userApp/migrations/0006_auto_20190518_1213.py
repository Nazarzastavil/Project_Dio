# Generated by Django 2.2 on 2019-05-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0005_auto_20190518_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventprofile',
            name='place',
        ),
        migrations.AlterField(
            model_name='eventprofile',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='eventprofile',
            name='date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='eventprofile',
            name='group',
            field=models.CharField(default='', max_length=100),
        ),
    ]
