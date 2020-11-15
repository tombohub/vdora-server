from django.db import models
from django.db.models.fields import CharField


class Product(models.Model):
    name = CharField(max_length=100)
    size = CharField(max_length=5, null=True, blank=True)
    color = CharField(max_length=20, null=True, blank=True)
    sku = CharField(max_length=20)
