# Generated by Django 2.0.4 on 2018-05-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DogGroom', '0002_remove_dog_xxx'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(null=True),
        ),
    ]