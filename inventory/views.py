import sys
from django.core.checks.messages import Error
from django.db import models
from rest_framework import viewsets, mixins, views, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_pivot.pivot import pivot
from .models import Transaction, TransactionType

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
        stock['Total'] = stock['Port Hope'] + \
            stock['Oshawa Centre'] + stock['In-house']

    nooks_total = Transaction.objects.filter(
        location=1).aggregate(models.Sum('quantity'))  # id 1 is Port Hope
    in_house_total = Transaction.objects.filter(
        location=2).aggregate(models.Sum('quantity'))  # id 2 is In-house
    oshawa_total = Transaction.objects.filter(
        location=4).aggregate(models.Sum('quantity'))  # id 4 is Oshawa

    return Response(stocks)


class ProductTranfer(views.APIView):
    def post(self, request):
        '''
        Received Product Tranfer Form data from frontend and create 2 transaction.
        One negative for product going out of location.
        One positive for product going inro location
        '''

        # ------------------------------------ out ----------------------------------- #

        def out_transaction():
            '''
            create a record for Out tranfer - product leaving the location
            '''
            type_id = TransactionType.objects.get(name="Out").id
            data = {
                'date': request.data['date'],
                'product': request.data['productId'],
                'type': type_id,
                # negative because product leaving this location
                'quantity': -request.data['quantity'],
                'location': request.data['fromLocationId'],
                'note': request.data['note']
            }

            serializer = TransactionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return {'success': True, 'data': serializer.data}
            return {'success': False, 'errors': serializer.errors}

        # ------------------------------------ in ------------------------------------ #

        def in_transaction():
            '''
            create a record for In transaction - product coming to location
            '''
            type_id = TransactionType.objects.get(name="In").id
            data = {
                'date': request.data['date'],
                'product': request.data['productId'],
                'type': type_id,
                'quantity': request.data['quantity'],
                'location': request.data['toLocationId'],
                'note': request.data['note']
            }

            serializer = TransactionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return {'success': True, 'data': serializer.data}
            return {'success': False, 'errors': serializer.errors}

        # insert transactions
        try:
            out_response = out_transaction()
            in_response = in_transaction()
        except Exception as error:
            # error = sys.exc_info()[0]
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if out_response['success'] and in_response['success']:
            return Response({
                'outTransaction': out_response['data'],
                'inTransaction': in_response['data']
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'outTrancaction': out_response['errors'],
                'inTransaction': in_response['errors']
            }, status=status.HTTP_400_BAD_REQUEST)
