from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, PublicMenuAPIView

router_menu = DefaultRouter()
router_menu.register(
    prefix="menu", basename="menu", viewset=MenuViewSet)


urlpatterns = [
    path("public/menus", PublicMenuAPIView.as_view(), name="public_menus"),
]
