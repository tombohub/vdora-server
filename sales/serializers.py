from .models import Sale, NooksPayoutSchedule
from rest_framework import serializers


class SaleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sale
        fields = '__all__'
        depth = 1


class NooksPayoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NooksPayoutSchedule
        fields = '__all__'
