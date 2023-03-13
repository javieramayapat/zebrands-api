from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer to return information from the users"""

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer to register users and add role is_staff"""

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer to update basic values form the user"""

    class Meta:
        model = User
        fields = ["first_name", "last_name", "user_name", "password" "email"]
