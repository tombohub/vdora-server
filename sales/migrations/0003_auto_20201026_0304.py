# Generated by Django 3.1.2 on 2020-10-26 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20201025_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='hst',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='net',
        ),
    ]