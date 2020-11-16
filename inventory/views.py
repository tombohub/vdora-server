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
def inventory_stock(request):
    stock = pivot(Transaction, 'product__name',
                  'location__name', 'quantity')
    return Response(stock)
