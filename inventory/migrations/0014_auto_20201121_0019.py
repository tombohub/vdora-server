# Generated by Django 3.1.2 on 2020-11-21 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_kaka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
