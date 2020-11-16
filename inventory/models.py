from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=5, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    sku = models.CharField(max_length=20)


class Location(models.Model):
    location = models.CharField(max_length=20)


class TransactionType(models.Model):
    type = models.CharField(max_length=20)


class Transaction(models.Model):
    TYPE_CHOICES = [('In', 'In'), ('Out', 'Out'), ('Sale', 'Sale')]
    LOCATION_CHOICES = [('Nooks', 'Nooks'), ('In-house', 'In-house')]

    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    note = models.TextField(null=True)
