from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.api.views import UserModelViewSet

urlpatterns = [
    # authentication
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router_user = DefaultRouter()

router_user.register(
    prefix='users',
    basename='users',
    viewset=UserModelViewSet
)
