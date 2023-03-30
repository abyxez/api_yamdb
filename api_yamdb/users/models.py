from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import datetime
from datetime import timedelta
import jwt
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user


class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin')
    ]
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Пользовательская роль',
        max_length=20,
        choices=ROLE_CHOICES,
        default='user'
    )
    email = models.EmailField(
        blank=False,
        unique=True
    )
    objects = UserManager()

    def _generate_jwt_token(self):
        dt = datetime.datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token


class UserConfirmation(models.Model):
    confirmation_code = models.CharField(
        max_length=6,
        blank=False,
        null=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
