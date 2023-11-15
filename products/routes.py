from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router_products = DefaultRouter()
router_products.register(
    prefix='products', basename='products', viewset=ProductViewSet)
