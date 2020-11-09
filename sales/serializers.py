from .models import Sale
from rest_framework import serializers


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'date', 'sku', 'product', 'quantity', 'price']
