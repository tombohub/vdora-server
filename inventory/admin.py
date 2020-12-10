from django.contrib import admin
from .models import Product, Location, Transaction, TransactionType


class TransactionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Transaction._meta.fields]


admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionType)
