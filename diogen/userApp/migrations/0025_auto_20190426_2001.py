# Generated by Django 2.2 on 2019-04-26 15:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0024_auto_20190426_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicianprofile',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 26, 15, 1, 0, 858203, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='musicianprofile',
            name='soundcloud',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 26, 15, 1, 0, 857203, tzinfo=utc)),
        ),
    ]
