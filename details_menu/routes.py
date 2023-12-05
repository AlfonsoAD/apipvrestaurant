from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DetailsMenuViewSet, DetailsMenuAPIView

router_details_menu = DefaultRouter()
router_details_menu.register(
    prefix="details_menu", basename="details_menu", viewset=DetailsMenuViewSet)

urlpatterns = [
    path('productsMenu/<int:idMenu>/',
         DetailsMenuAPIView.as_view(), name='filterByMenu'),
]
