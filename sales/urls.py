from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sales', views.SaleViewSet)
router.register('nooks-payout-schedules', views.NooksPayoutViewSet)
router.register('koko', views.Koko, basename='koko')


urlpatterns = [
    path('', include(router.urls)),
    path('sales/reports/monthly/', views.monthly_sales),
    path('sales/reports/nooks-payouts/', views.nooks_payouts),

]
