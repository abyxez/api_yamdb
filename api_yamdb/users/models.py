from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = [
    ('anonymous', 'anonymous'),
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin')
]


class User(AbstractUser):
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
