from django.db.models import Sum, F, Count

from rest_framework import viewsets, filters, permissions, views, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .serializers import SaleSerializer, NooksPayoutSerializer
from .models import Sale, NooksPayoutSchedule
from inventory.models import Transaction
from django_pivot.pivot import pivot


class SaleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sales to be edited
    """
    queryset = Sale.objects.all().order_by('-date')
    serializer_class = SaleSerializer

    # allow for postmark app to send emails
    def get_permissions(self):
        if self.action == 'parse_email':
            self.permission_classes = permissions.AllowAny
        return super().get_permissions()

    @action(detail=False)
    def product_sales(self, request):
        '''
        products per items sold report
        '''
        product_sales = Transaction.objects.filter(type=1).values(
            'product__name').annotate(Count('product'))

        return Response(product_sales, status=status.HTTP_200_OK)

    @action(methods='POST', detail=False)
    def parse_email(self, request):
        return Response(request.data, status=status.HTTP_200_OK)


class NooksPayoutViewSet(viewsets.ModelViewSet):
    """
    API endpoints for nooks payouts schedules data
    """
    queryset = NooksPayoutSchedule.objects.all().order_by('-payout_date')
    serializer_class = NooksPayoutSerializer


class ReportsViewSet(viewsets.ViewSet):
    '''
    View set for various sale reports
    '''

    @action(detail=False)
    def product_sales(self, request):
        '''
        products per items sold report
        '''
        product_sales = Transaction.objects.filter(type="Sale").values(
            'product__name').annotate(Count('product'))

        return Response(product_sales, status=status.HTTP_200_OK)


@api_view()
def monthly_sales(request):
    monthly_sales = pivot(Sale, 'date__month', 'channel', 'price', default=0)

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
