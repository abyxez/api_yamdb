from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, role=None, bio=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            role=role,
            bio=bio
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
        self, username, email,
        password, role=None, bio=None
    ):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password, role, bio)
        user.is_superuser = True
        user.is_staff = True
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
        blank=True
    )
    role = models.CharField(
        'Пользовательская роль',
        max_length=20,
        choices=ROLE_CHOICES,
        default='user'
    )
    email = models.EmailField(
        max_length=254,
        blank=False,
        null=False,
        unique=True
    )
    objects = UserManager()
