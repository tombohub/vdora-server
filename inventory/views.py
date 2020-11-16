from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_pivot.pivot import pivot

from .serializers import ProductSerializer
from .models import Product, Transaction


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


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
