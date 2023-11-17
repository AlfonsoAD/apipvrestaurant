"""
URL configuration for pvrestaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from categorys.routes import router_categorys
from products.routes import router_products
from tables.routes import router_table
from menus.routes import router_menu
from details_menu.routes import router_details_menu
from orders.routes import router_order
from details_order.routes import router_details_order
from product_notes.routes import router_product_notes
from box_oppenings.routes import router_box_oppenings
from box_cuts.routes import router_box_cuts
from sales.routes import router_sales

schema_view = get_schema_view(
    openapi.Info(
        title="PV Restaurant API",
        default_version='v1',
        description="Proyecto final python",
        terms_of_service="",
        contact=openapi.Contact(email="andrajesus2015@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("users.routes")),
    path("api/", include(router_categorys.urls)),
    path("api/", include(router_products.urls)),
    path("api/", include(router_table.urls)),
    path("api/", include(router_menu.urls)),
    path("api/", include(router_details_menu.urls)),
    path("api/", include(router_order.urls)),
    path("api/", include(router_details_order.urls)),
    path("api/", include(router_product_notes.urls)),
    path("api/", include(router_box_oppenings.urls)),
    path("api/", include(router_box_cuts.urls)),
    path("api/", include(router_sales.urls)),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
