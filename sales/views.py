from django.db.models import Sum, F

from rest_framework import viewsets, filters, permissions, views
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SaleSerializer, NooksPayoutSerializer
from .models import Sale, NooksPayoutSchedule


class SaleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sales to be edited
    """
    queryset = Sale.objects.all().order_by('-date')
    serializer_class = SaleSerializer


class NooksPayoutViewSet(viewsets.ModelViewSet):
    """
    API endpoints for nooks payouts schedules data
    """
    queryset = NooksPayoutSchedule.objects.all().order_by('-payout_date')
    serializer_class = NooksPayoutSerializer


@api_view()
def monthly_sales(request):
    monthly_sales = Sale.objects.values(
        'date__month').annotate(Sum('price'))
    return Response(monthly_sales)


@api_view()
def nooks_payouts(request):
    """Nooks payouts schedule with the date when check can be picked up.

    Response: payout date, 
            id from nooks payouts schedule table
            sum to be paid
            is_picked - is checked picke up or not
    """
    payouts = Sale.objects.filter(channel='Nooks', nooks_payout_schedule__isnull=False).values(
        payout_date=F('nooks_payout_schedule__payout_date'),
        is_picked=F('nooks_payout_schedule__is_picked'),
        payout_id=F('nooks_payout_schedule__id')).annotate(sum=Sum('price'))
    return Response(payouts)
