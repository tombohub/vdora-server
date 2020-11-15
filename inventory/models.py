from django.db import models
from django.db.models.fields import CharField


class Product(models.Model):
    name = CharField(max_length=100)
    size = CharField(max_length=5)
    color = CharField(max_length=20)
    sku = CharField(max_length=20)
