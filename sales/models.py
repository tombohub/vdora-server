from django.db import models
from django.db.models.fields import BooleanField, DateField
from inventory.models import Product, Transaction


class NooksPayoutSchedule(models.Model):
    start_date = DateField()
    end_date = DateField()
    payout_date = DateField()
    is_picked = BooleanField()

    def __str__(self) -> str:
        return str(self.payout_date)


class Sale(models.Model):
    date = models.DateField()
    sale_id = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    channel = models.CharField(max_length=100)
    nooks_payout_schedule = models.ForeignKey(
        NooksPayoutSchedule, on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.date}, {self.product}'
