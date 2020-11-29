
from django.db import models


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
        return self.name


class TransactionType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Transaction(models.Model):
    date = models.DateField()
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT)
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    note = models.TextField(null=True, blank=True)
    sale = models.ForeignKey('sales.Sale', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.date}, {self.product.name}, {self.type.name}'


class Test(models.Model):
    koko = models.CharField(max_length=94)
    momo = models.IntegerField(null=True)


class Kaka(models.Model):
    kaka = models.IntegerField()
    riri = models.ForeignKey(Test, on_delete=models.CASCADE)
