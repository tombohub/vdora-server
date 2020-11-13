from rest_framework import viewsets, filters, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SaleSerializer
from .models import Sale


class SaleViewSet(viewsets.ModelViewSet):
    """API endpoint that allows sales to be edited
    """
    queryset = Sale.objects.all().order_by('-date')
    serializer_class = SaleSerializer

    # permission_classes = [permissions.IsAuthenticated]


@api_view()
def monthly_sales(request):
    sales = Sale.objects.all()
    serializer = SaleSerializer(sales, many=True, context={'request': request})
    return Response(serializer.data)
