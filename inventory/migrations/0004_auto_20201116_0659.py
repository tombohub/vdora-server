# Generated by Django 3.1.2 on 2020-11-16 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20201116_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.location'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.transactiontype'),
        ),
    ]