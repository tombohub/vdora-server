from django.db import models
from rest_framework import viewsets, generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_pivot.pivot import pivot

from .serializers import ProductSerializer, LocationSerializer, TransactionSerializer
from .models import Location, Product, Transaction


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LocationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


@api_view()
def inventory_stocks(request):
    """
    Current Inventory stock for each product. Divided by each warehouse location
    """
    stocks = pivot(Transaction, 'product__name',
                   'location__name', 'quantity', default=0)
    for stock in stocks:
        stock['Total'] = stock['Nooks'] + stock['In-house']

    return Response(stocks)
