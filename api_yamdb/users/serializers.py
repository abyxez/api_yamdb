from rest_framework import serializers
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
