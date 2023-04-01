from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField(verbose_name='Category name',
                            max_length=256, )
    slug = models.SlugField(unique=True,
                            max_length=50, )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Genre name',
                            max_length=256, )
    slug = models.SlugField(unique=True,
                            max_length=50, )

    def __str__(self):
        return self.name


class Title(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 verbose_name='Slug of category', )
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Slug of genre', )
    name = models.CharField(max_length=256,
                            verbose_name='Name', )
    year = models.IntegerField(verbose_name='Publication year',
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(datetime.now().year)], )
    description = models.TextField(verbose_name='Description',
                                   null=True,
                                   blank=True, )

    class Meta:
        default_related_name = 'titles'


class Review(models.Model):
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='Text of the review', )
    score = models.IntegerField(default=5,
                                verbose_name='Rating score',
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(10)], )
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE, )

    class Meta:
        default_related_name = 'reviews'


class Comment(models.Model):
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE, )
    text = models.TextField(verbose_name='Text to comment', )
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True, )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE, )

    class Meta:
        default_related_name = 'comments'
