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
        password, role='user', bio=''
    ):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password, role, bio)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin')
    ]
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        'Пользовательская роль',
        max_length=20,
        choices=ROLE_CHOICES,
        default=USER
    )
    email = models.EmailField(
        max_length=254,
        blank=False,
        null=False,
        unique=True
    )
    objects = UserManager()

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser
