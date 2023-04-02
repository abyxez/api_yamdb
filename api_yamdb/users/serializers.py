from rest_framework import serializers

from .models import User


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, allow_blank=False)
    email = serializers.EmailField()

    class Meta:
        fields = (
            'username',
            'email'
        )


class GetTokenSerializer(serializers.Serializer):
    class Meta:
        fields = (
            'username',
            'confirmation_code'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        read_only_fields = ('role',)

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Нельзя использовать это имя')
        return value
