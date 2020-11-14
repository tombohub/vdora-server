from .models import Sale, NooksPayoutSchedule
from rest_framework import serializers


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = ['url', 'id', 'date', 'sku', 'product', 'quantity', 'price']


class NooksPayoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NooksPayoutSchedule
        fields = '__all__'
