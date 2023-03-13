from rest_framework.viewsets import ModelViewSet

from views.api.serializers import ViewSerializer
from views.models import View


class ViewsModelViewSet(ModelViewSet):
    serializer_class = ViewSerializer
    queryset = View.objects.all()
    http_method_names = ["get"]
