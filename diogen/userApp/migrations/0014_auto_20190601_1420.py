# Generated by Django 2.2 on 2019-06-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0013_auto_20190601_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventprofile',
            name='group',
        ),
        migrations.AddField(
            model_name='eventprofile',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, to='userApp.GroupProfile'),
        ),
    ]