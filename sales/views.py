from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .models import Sale
from rest_framework import viewsets, filters
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication
from .serializers import SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    """API endpoint that allows sales to be edited
    """
    queryset = Sale.objects.all().order_by('-date')
    serializer_class = SaleSerializer

    # permission_classes = [permissions.IsAuthenticated]
