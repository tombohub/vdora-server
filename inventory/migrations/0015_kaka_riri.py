# Generated by Django 3.1.2 on 2020-11-23 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20201121_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='kaka',
            name='riri',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.test'),
            preserve_default=False,
        ),
    ]
