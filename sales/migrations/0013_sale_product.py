# Generated by Django 3.1.2 on 2020-11-29 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_kaka_riri'),
        ('sales', '0012_remove_sale_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='inventory.product'),
        ),
    ]
