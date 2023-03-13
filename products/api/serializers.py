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


class ProductPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'price',
        ]
