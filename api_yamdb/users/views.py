from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .permissions import IsAdminOnly
from .serializers import GetTokenSerializer, SignUpSerializer, UserSerializer, UserSerializerMe


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(
                username=serializer.data['username']
            ).exists():
                user = User.objects.get(username=serializer.data['username'])
                if user.email == serializer.data['email']:
                    token = default_token_generator.make_token(user)
                    send_mail(
                        'Please check your confirmation code',
                        f'{user.username}! Your confirmation code: {token}',
                        'crew_74@ya.ru',
                        (serializer.data['email'],),
                        fail_silently=False
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(
                    {'Введенный email не принадлежит этому пользователю'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.get(username=serializer.data['username'])
                token = default_token_generator.make_token(user)
                send_mail(
                    'Please check your confirmation code',
                    f'Hey, {user.username}! Your confirmation code: {token}',
                    'crew_74@ya.ru',
                    (serializer.data['email'],),
                    fail_silently=False
                )
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )


@api_view(['POST'])
def get_jwt_token(request):
    if request.method == 'POST':
        serializer = GetTokenSerializer(data=request.data)
        user = get_object_or_404(
            User,
            username=serializer.initial_data['username']
        )
        token = serializer.initial_data['confirmation_code']
        if default_token_generator.check_token(user, token):
            jwt_token = AccessToken.for_user(user)
            return Response(
                {'token': f'{jwt_token}'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'Введен неверный confirmation_code'},
            status=status.HTTP_400_BAD_REQUEST
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOnly,)
    lookup_field = 'username'


@api_view(['GET', 'PATCH'])
def user_me(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            serializer = UserSerializerMe(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'Анонимный пользователь'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    if request.method == 'PATCH':
        if request.user.is_authenticated:
            serializer = UserSerializerMe(
                request.user,
                data=request.data,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'Анонимный пользователь'},
            status=status.HTTP_401_UNAUTHORIZED
        )
