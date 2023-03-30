from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

User = get_user_model()

ROLES = (
    'User',
    'Moderator',
    'Administrator',
    'Superuser',
)

"""
class User(AbstractUser):
    bio = models.TextField('Biography', )
    role = models.CharField('Role of the user',
                            max_length=13,
                            choices=ROLES,
                            default='User')
"""

class Category(models.Model):
    name = models.CharField('Category name',
                            max_length=256, )
    slug = models.SlugField(unique=True,
                            max_length=50, )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Genre name',
                            max_length=256, )
    slug = models.SlugField(unique=True,
                            max_length=50, )

    def __str__(self):
        return self.name


class Title(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 verbose_name='Slug of category', )
    genre = models.ForeignKey(Genre,
                              on_delete=models.PROTECT,
                              verbose_name='Slug of genre', )
    name = models.CharField(max_length=256,
                            verbose_name='Name', )
    year = models.DateField('Publication year', )
    description = models.TextField('Description',
                                   null=True,
                                   blank=True, )

    class Meta:
        default_related_name = 'titles'


class Review(models.Model):
    title_id = models.ForeignKey(Title,
                                 on_delete=models.CASCADE,
                                 related_name='reviews', )
    text =  models.TextField('Text of the review', )
    score = models.IntegerField(default=5,
                                verbose_name='Rating score',
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(10)],)


class Comment(models.Model):
    title_id = models.ForeignKey(Title,
                                 on_delete=models.CASCADE, )
    review_id = models.ForeignKey(Review,
                                  on_delete=models.CASCADE, )
    text = models.TextField()

    class Meta:
        default_related_name = 'comments'
