from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=5, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    sku = models.CharField(max_length=20)


class Transaction(models.Model):
    TYPE_CHOICES = [('In', 'In'), ('Out', 'Out'), ('Sale', 'Sale')]
    LOCATION_CHOICES = [('Nooks', 'Nooks'), ('In-house', 'In-house')]

    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    quantity = models.IntegerField()
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    note = models.TextField()
