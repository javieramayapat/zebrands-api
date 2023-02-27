from django.views import View
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from products.api.serializers import ProductSerializer, ProductPatchSerializer
from products.models import Product
from views.models import View
from products.api.permissions import IsAdminOrReadOnly


class ProductsModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'sku'
    http_method_names = ['get', 'patch', 'post', 'delete']

    def create(self, request, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        identifier = Product.objects.count() + 1
        sku = f"{request.data['name'][:3].upper()}-{request.data['brand'][:3].upper()}-{identifier:04}"
        serializer.validated_data['sku'] = sku

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, sku=None, **kwargs):
        if sku is not None:
            product = get_object_or_404(Product, sku=sku)
        else:
            product = self.get_object()
        view = View.objects.create()
        product.views.add(view)
        return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
    