from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer


class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    ordering = ['-created_at']
    queryset = Category.objects.all()