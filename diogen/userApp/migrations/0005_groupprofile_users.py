# Generated by Django 2.2 on 2019-05-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0004_remove_groupprofile_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupprofile',
            name='users',
            field=models.ManyToManyField(to='userApp.PersonProfile'),
        ),
    ]