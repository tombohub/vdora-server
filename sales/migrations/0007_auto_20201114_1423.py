# Generated by Django 3.1.2 on 2020-11-14 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_sale_payout_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='payout_schedule',
            new_name='nooks_payout_schedule',
        ),
    ]