from django.urls import path
from .views import UserRegisterView, UserView, UsersView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import UsersView, CustomTokenObtainPairView

urlpatterns = [
    path('auth/register', UserRegisterView.as_view(), name='register'),
    # path('auth/login', TokenObtainPairView.as_view(), name='login'),
    path('auth/login', CustomTokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path("auth/me", UserView.as_view()),
]


router_users = DefaultRouter()
router_users.register(prefix='users', basename='users', viewset=UsersView)
