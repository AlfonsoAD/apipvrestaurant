from django.urls import path
from .views import UserRegisterView, UsersView, UserPasswordUpdateView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import UsersView, CustomTokenObtainPairView, TokenValidationView

urlpatterns = [
    path('auth/register', UserRegisterView.as_view(), name='register'),
    # path('auth/login', TokenObtainPairView.as_view(), name='login'),
    path('auth/login', CustomTokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path("auth/renew", TokenValidationView.as_view(), name="token_validation"),
    path("auth/changepassword/<int:pk>/", UserPasswordUpdateView.as_view({'put': 'update'}),
         name="change_password"),
]


router_users = DefaultRouter()
router_users.register(prefix='users', basename='users', viewset=UsersView)
