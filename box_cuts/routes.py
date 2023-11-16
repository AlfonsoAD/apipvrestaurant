from rest_framework.routers import DefaultRouter
from .views import BoxCutViewSet

router_box_cuts = DefaultRouter()
router_box_cuts.register(
    prefix="box_cuts", basename='box_cuts', viewset=BoxCutViewSet)
