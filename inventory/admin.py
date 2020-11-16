from django.contrib import admin
from .models import Product, Location, Transaction, TransactionType

admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Transaction)
admin.site.register(TransactionType)
