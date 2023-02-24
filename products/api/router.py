from rest_framework.routers import DefaultRouter
from products.views import ProductsModelViewSet


router_product = DefaultRouter()

router_product.register(
    prefix='products',
    basename='products',
    viewset=ProductsModelViewSet,
)