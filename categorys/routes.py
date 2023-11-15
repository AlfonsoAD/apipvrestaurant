from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router_categorys = DefaultRouter()
router_categorys.register(
    prefix='categorys', basename='categorys', viewset=CategoryViewSet)
