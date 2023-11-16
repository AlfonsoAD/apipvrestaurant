from rest_framework.routers import DefaultRouter
from .views import MenuViewSet

router_menu = DefaultRouter()
router_menu.register(
    prefix="menu", basename="menu", viewset=MenuViewSet)
