from django.db.models import Sum

from rest_framework import viewsets, filters, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SaleSerializer
from .models import Sale, NooksPayoutSchedule


class SaleViewSet(viewsets.ModelViewSet):
    """API endpoint that allows sales to be edited
    """
    queryset = Sale.objects.all().order_by('-date')
    serializer_class = SaleSerializer

    # permission_classes = [permissions.IsAuthenticated]


@api_view()
def monthly_sales(request):
    monthly_sales = Sale.objects.values(
        'date__month').annotate(Sum('price'))
    return Response(monthly_sales)


@api_view()
def nooks_payouts(request):
    pass
