# Generated by Django 2.2 on 2019-06-01 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0008_acceptedevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptedevent',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]