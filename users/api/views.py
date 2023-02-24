from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from users.api.serializer import UserSerializer, UserRegisterSerializer

from users.models import User


class UserViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def create(self, request):
        serializer = UserRegisterSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'patch', 'delete']
