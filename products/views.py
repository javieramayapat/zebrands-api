from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from products.api.serializers import ProductSerializer
from products.models import Product


class ProductsModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    http_method_names = ['post', 'patch', 'delete']
