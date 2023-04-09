from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from users.models import User


class Category(models.Model):
    name = models.CharField('Категория',
                            max_length=256, )
    slug = models.SlugField(unique=True,
                            max_length=50, )

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'categories'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField('Жанр',
                            max_length=256, )
    slug = models.SlugField(unique=True,
                            max_length=50, )

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'genres'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 verbose_name='Категория', )
    genre = models.ManyToManyField(Genre,
                                   through='GenreTitle')
    name = models.CharField('Произведение',
                            max_length=256, )
    year = models.PositiveSmallIntegerField(
        'Год публикации',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(timezone.now().year)
        ]
    )
    description = models.TextField('Описание',
                                   blank=True, )

    def __str__(self) -> str:
        return self.name

    class Meta:
        default_related_name = 'titles'
        verbose_name_plural = 'Произведения'


class Review(models.Model):
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              verbose_name='Произведение', )
    text = models.TextField('Отзыв', )
    score = models.PositiveSmallIntegerField('Рейтинг',
                                             default=5,
                                             validators=[
                                                 MinValueValidator(1),
                                                 MaxValueValidator(10)])
    pub_date = models.DateTimeField('Дата публикации',
                                    auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор', )

    def __str__(self) -> str:
        return self.text

    class Meta:
        default_related_name = 'reviews'
        unique_together = ('title', 'author',)
        verbose_name_plural = 'Отзывы'


class Comment(models.Model):
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               verbose_name='Отзыв', )
    text = models.TextField(verbose_name='Комментарий', )
    pub_date = models.DateTimeField('Дата публикации',
                                    auto_now_add=True, )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор', )

    def __str__(self) -> str:
        return self.text

    class Meta:
        default_related_name = 'comments'
        verbose_name_plural = 'Комментарии'


class GenreTitle(models.Model):
    title = models.ForeignKey(Title,
                              verbose_name='Произведение',
                              related_name='titles',
                              on_delete=models.CASCADE, )
    genre = models.ForeignKey(Genre,
                              verbose_name='Жанр',
                              related_name='genres',
                              on_delete=models.CASCADE, )

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Жанры произведения'
