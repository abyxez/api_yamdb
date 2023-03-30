from .serializers import SignUpSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from random import choices
import string
from .models import UserConfirmation, User


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

