# Generated by Django 2.2 on 2019-04-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0012_auto_20190426_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='personprofile',
            name='adress',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='birth_date',
            field=models.DateField(default='1999-01-01'),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]
