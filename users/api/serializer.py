from rest_framework import serializers
from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]

        extra_kwargs = {'is_staff': {'default': True}}

    def create(self, validated_data):
        is_staff = validated_data.get('is_staff', True)

        # Create the new user with teh validated data and encrypted password
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=is_staff
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'last_name',
            'email',
            'username',
        ]
