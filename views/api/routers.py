from rest_framework.routers import DefaultRouter

from views.views import ViewsModelViewSet

router_view = DefaultRouter()

router_view.register(
    prefix="views",
    basename="views",
    viewset=ViewsModelViewSet,
)
