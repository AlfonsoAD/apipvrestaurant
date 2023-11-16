from rest_framework.routers import DefaultRouter
from .views import TableViewSet

router_table = DefaultRouter()
router_table.register(prefix="tables", basename="tables", viewset=TableViewSet)
