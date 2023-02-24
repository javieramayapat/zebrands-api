from rest_framework import serializers
from categories.models import Category
from users.api.serializer import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'description',
            'created_at'
        ]
