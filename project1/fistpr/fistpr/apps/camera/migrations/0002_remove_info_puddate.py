# Generated by Django 3.0.7 on 2020-06-10 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='PudDate',
        ),
    ]
