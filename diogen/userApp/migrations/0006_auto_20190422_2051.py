# Generated by Django 2.2 on 2019-04-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0005_auto_20190420_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
            preserve_default=False,
        ),
    ]