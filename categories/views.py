from rest_framework.viewsets import ModelViewSet

from categories.api.permissions import IsAdminOrReadOnly
from categories.api.serializers import CategorySerializer
from categories.models import Category


class CategoryModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('-created_at')