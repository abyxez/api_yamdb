from .serializers import SignUpSerializer, GetTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from random import choices
import string
from .models import UserConfirmation, User
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            current_conf_code = ''.join(choices(string.digits, k=4))
            UserConfirmation.objects.create(
                confirmation_code=current_conf_code,
                user=User.objects.get(username=serializer.data['username'])
            )
            send_mail(
                'Please check your confirmation code',
                f'Your confirmation code: {current_conf_code}',
                'crew_74@ya.ru',
                (serializer.data['email'],),
                fail_silently=False
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_jwt_token(request):
    if request.method == 'POST':
        serializer = GetTokenSerializer(data=request.data)
        user = get_object_or_404(
            User,
            username=serializer.initial_data['username']
        )
        user_confirmation = get_object_or_404(UserConfirmation, user=user)
        passed_confirm_code = user_confirmation.confirmation_code
        if serializer.initial_data['confirmation_code'] == passed_confirm_code:
            jwt_token = user._generate_jwt_token()
            return Response(
                {'token': jwt_token},
                status=status.HTTP_200_OK
            )
        return Response(
            {'Введен неверный confirmation_code'},
            status=status.HTTP_400_BAD_REQUEST
        )
