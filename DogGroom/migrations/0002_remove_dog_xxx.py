# Generated by Django 2.0.4 on 2018-05-03 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DogGroom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='xxx',
        ),
    ]