# Generated by Django 3.1.2 on 2020-11-13 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20201026_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='channel',
            field=models.CharField(default='Nooks', max_length=100),
            preserve_default=False,
        ),
    ]