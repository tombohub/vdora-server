# Generated by Django 3.1.2 on 2020-11-17 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_delete_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='inventory.product'),
        ),
    ]
