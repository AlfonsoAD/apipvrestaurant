from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router_order = DefaultRouter()
router_order.register(prefix="orders", basename="orders", viewset=OrderViewSet)
