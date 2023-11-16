from rest_framework.routers import DefaultRouter
from .views import DetailsOrderViewSet

router_details_order = DefaultRouter()
router_details_order.register(
    prefix='details_order', basename='details_order', viewset=DetailsOrderViewSet)
