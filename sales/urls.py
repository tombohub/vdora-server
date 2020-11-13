from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sales', views.SaleViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('sales/reports/monthly', views.monthly_sales),
]
