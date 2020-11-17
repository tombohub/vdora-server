from django.conf.urls import url
from django.db import router
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('locations', views.LocationViewSet)
router.register('transactions', views.TransactionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('reports/stocks/', views.inventory_stocks),
]
