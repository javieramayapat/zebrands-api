from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from users.api.serializer import UserSerializer, UserRegisterSerializer, UserUpdateSerializer
from drf_yasg.utils import swagger_auto_schema

from users.models import User


class UserModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-id')
    http_method_names = ['get', 'post', 'put', 'delete']

    @swagger_auto_schema(request_body=UserRegisterSerializer)
    def create(self, request, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.get('password')
        user = serializer.save()
        user.is_staff = True
        user.set_password(password)
        user.save()
        return Response(data=UserSerializer(user).data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=UserUpdateSerializer)
    def put(self, request, pk=None, **kwargs):
        user = self.get_object()
        serializer = UserUpdateSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        password = serializer.validated_data.get('password')
        if password:
            user.set_password(password)
            user.save()
        return Response(data=UserSerializer(user).data, status=status.HTTP_200_OK)
