# Generated by Django 3.1.2 on 2020-11-29 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0014_remove_sale_sku'),
        ('inventory', '0015_kaka_riri'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.sale'),
        ),
    ]