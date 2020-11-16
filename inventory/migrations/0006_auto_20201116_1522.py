# Generated by Django 3.1.2 on 2020-11-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='transactiontype',
            old_name='type',
            new_name='name',
        ),
        migrations.AddField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]