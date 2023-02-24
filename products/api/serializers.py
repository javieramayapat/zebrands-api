from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = ('sku',)
        fields = [
            'id',
            'sku',
            'name',
            'brand',
            'description',
            'price',
            'user',
            'category',
            'created_at',
            'updated_at',
        ]

    def save(self, **kwargs):
        name = self.validated_data.get('name', '')
        brand = self.validated_data.get('brand', '')
        description = self.validated_data.get('description', '')
        prince = self.validated_data.get('price', '')
        category = self.validated_data.get('category', '')
        user = self.validated_data.get('user', '')
        identifier = Product.objects.count() + 1
        sku = f"{name[:4].upper()}-{brand[:4].upper()}-{identifier:04}"

        self.validated_data['sku'] = sku

        return super().save(**kwargs)
