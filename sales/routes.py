from rest_framework.routers import DefaultRouter
from .views import SaleViewSet

router_sales = DefaultRouter()
router_sales.register(prefix='sales', basename='sales', viewset=SaleViewSet)
