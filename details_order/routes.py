from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DetailsOrderViewSet, DetailOrderAPIView

router_details_order = DefaultRouter()
router_details_order.register(
    prefix='details_order', basename='details_order', viewset=DetailsOrderViewSet)

urlpatterns = [
    path('detailsOrder/<int:order_id>',
         DetailOrderAPIView.as_view(), name='filterByOrder'),
]
