from django.db import models
from django.db.models.deletion import CASCADE


class Product(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=5, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    sku = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.location


class TransactionType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.type


class Transaction(models.Model):

    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    note = models.TextField(null=True)

    def __str__(self) -> str:
        return self.product
