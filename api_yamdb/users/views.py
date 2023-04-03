from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated

from .models import User
from .permissions import IsAdminOnly
from .serializers import (
    GetTokenSerializer, SignUpSerializer, UserCreateSerializer,
    UserSerializerAdmin, UserSerializerMe
)


def send_code(user, token, email):
    send_mail(
        'Please check your confirmation code',
        f'{user}! Your confirmation code: {token}',
        'crew_74@ya.ru',
        (email,),
        fail_silently=False
    )


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
                    send_code(
                        user.username,
                        token,
                        serializer.data['email']
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(
                    {'Введенный email не принадлежит этому пользователю'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer = UserCreateSerializer(data=request.data)
            if serializer.is_valid():
                if not User.objects.filter(
                    email=serializer.validated_data['email']
                ).exists():
                    serializer.save()
                    user = User.objects.get(
                        username=serializer.data['username']
                    )
                    token = default_token_generator.make_token(user)
                    send_code(
                        user.username,
                        token,
                        serializer.data['email']
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(
                    {'Пользователь с таким email уже существует'},
                    status=status.HTTP_400_BAD_REQUEST
                )
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
        if serializer.is_valid():
            user = get_object_or_404(
                User,
                username=serializer.validated_data['username']
            )
            token = serializer.initial_data['confirmation_code']
            if default_token_generator.check_token(user, token):
                jwt_token = AccessToken.for_user(user)
                return Response(
                    {'token': f'{jwt_token}'},
                    status=status.HTTP_200_OK
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'Введен неверный confirmation_code'},
            status=status.HTTP_400_BAD_REQUEST
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerAdmin
    permission_classes = (IsAuthenticated, IsAdminOnly)
    filter_backends = (SearchFilter, )
    search_fields = ('username', )
    lookup_field = 'username'
    http_method_names = ['get', 'post', 'patch', 'delete']


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
