from django.db import models
from django.db.models.fields import DateField


class NooksPayoutSchedule(models.Model):
    start_date = DateField()
    end_date = DateField()
    payout_date = DateField()


class Sale(models.Model):
    date = models.DateField()
    sale_id = models.IntegerField()
    sku = models.CharField(max_length=10)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    channel = models.CharField(max_length=100)
    nooks_payout_schedule = models.ForeignKey(
        NooksPayoutSchedule, on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self):
        return self.product
