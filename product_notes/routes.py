from rest_framework.routers import DefaultRouter
from .views import ProductNotesViewSet

router_product_notes = DefaultRouter()
router_product_notes.register(
    prefix='product_notes', basename='product_notes', viewset=ProductNotesViewSet)
