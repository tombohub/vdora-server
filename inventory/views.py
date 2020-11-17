from django.db import models
from rest_framework import viewsets, mixins, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_pivot.pivot import pivot
from .models import Transaction

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


class ProductTranfer(views.APIView):
    def post(self, request):
        date = request.data['date']
        product_id = request.data['productId']
        from_location_id = request.data['fromLocationId']
        to_location_id = request.data['toLocationId']
        quantity = request.data['quantity']
        note = request.data['note']

        transaction_type = 1

        transaction = Transaction(
            date=date, product_id=product_id, type_id=transaction_type, quantity=quantity, location_id=from_location_id, note=note)

        transaction.save()

        return Response('jasts')
