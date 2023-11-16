from rest_framework.routers import DefaultRouter
from .views import DetailsMenuViewSet

router_details_menu = DefaultRouter()
router_details_menu.register(
    prefix="details_menu", basename="details_menu", viewset=DetailsMenuViewSet)
