from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from products.api.serializers import ProductSerializer
from products.models import Product
from products.api.permissions import IsAdminOrReadOnly


class ProductsModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    http_method_names = ['get','post', 'patch', 'delete']
