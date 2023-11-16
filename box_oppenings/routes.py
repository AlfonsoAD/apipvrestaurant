from rest_framework.routers import DefaultRouter
from .views import BoxOppeningViewSet

router_box_oppenings = DefaultRouter()
router_box_oppenings.register(
    prefix='box_oppenings', viewset=BoxOppeningViewSet, basename='box_oppenings')
