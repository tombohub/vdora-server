# Generated by Django 3.1.2 on 2020-11-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='note',
            field=models.TextField(null=True),
        ),
    ]