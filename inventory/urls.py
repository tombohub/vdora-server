from django.conf.urls import url
from django.db import router
from django.urls import include, path
from rest_framework import routers
from rest_framework import urlpatterns
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('reports/stocks', views.inventory_stocks)
]
