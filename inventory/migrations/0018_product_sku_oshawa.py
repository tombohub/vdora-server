# Generated by Django 3.1.2 on 2020-12-08 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_auto_20201202_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku_oshawa',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]