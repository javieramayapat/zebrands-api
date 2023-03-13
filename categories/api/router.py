from rest_framework.routers import DefaultRouter

from categories.views import CategoryModelViewSet

router_category =  DefaultRouter()

router_category.register(
    prefix='categories',
    basename='categories',
    viewset=CategoryModelViewSet
)