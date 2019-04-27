# Generated by Django 2.2 on 2019-04-26 16:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0030_auto_20190426_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personprofile',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 4, 26, 16, 58, 3, 532305, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='company',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='genres',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='instruments',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]