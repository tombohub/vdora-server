from django.db import models


class Sale(models.Model):
    date = models.DateField()
    sale_id = models.IntegerField()
    sku = models.CharField(max_length=10)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.product
