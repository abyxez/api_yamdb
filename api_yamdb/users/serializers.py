from rest_framework import serializers

from .models import User


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, allow_blank=False)
    email = serializers.EmailField(max_length=254, allow_blank=False)

    class Meta:
        fields = (
            'username',
            'email'
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Имя me нельзя использовать')
        return value


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Имя me нельзя использовать')
        return value


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150, allow_blank=False,
    )
    confirmation_code = serializers.CharField(
        max_length=150, allow_blank=False
    )

    class Meta:
        fields = (
            'username',
            'confirmation_code'
        )


class UserSerializerMe(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        read_only_fields = ('role', )


class UserSerializerAdmin(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
