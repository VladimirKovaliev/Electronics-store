from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.apps import UsersConfig
from users.views import UserViewSet, UserCreateAPIView

app_name = UsersConfig.name  # Чтобы в корневой файл урлов подлючить работу с пользователями

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('create/', UserCreateAPIView.as_view(), name='user-create'),

              ] + router.urls
