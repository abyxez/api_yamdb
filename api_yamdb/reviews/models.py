from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',
                            max_length=256, )
    slug = models.SlugField(unique=True,
                            max_length=50, )

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'categories'


class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра',
                            max_length=256, )
    slug = models.SlugField(unique=True,
                            max_length=50, )

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'genres'


class Title(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 verbose_name='Категория', )
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Жанр', )
    name = models.CharField(max_length=256,
                            verbose_name='Название', )
    year = models.IntegerField(verbose_name='Год публикации',
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(datetime.now().year)], )
    description = models.TextField(verbose_name='Описание',
                                   null=True,
                                   blank=True, )

    class Meta:
        default_related_name = 'titles'


class Review(models.Model):
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              verbose_name='Произведения',)
    text = models.TextField(verbose_name='Текст отзыва', )
    score = models.IntegerField(default=5,
                                verbose_name='Рейтинг',
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(10)], )
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор',)

    class Meta:
        default_related_name = 'reviews'
        unique_together = ('title', 'author')


class Comment(models.Model):
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               verbose_name='Отзыв',)
    text = models.TextField(verbose_name='Текст комментария', )
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True, )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор',)

    class Meta:
        default_related_name = 'comments'
