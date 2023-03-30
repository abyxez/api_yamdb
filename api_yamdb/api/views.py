from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import (CategorySerializer, GenreSerializer, TitleSerializer,
                          ReviewSerializer, CommentSerializer)
from titles.models import Category, Genre, Title, Review, Comment


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', )
    pagination_class = (LimitOffsetPagination)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('name', )
    


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, )
    filterset_fields = ('category',
                        'genre',
                        'name',
                        'year', )


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    #pagination_class = PageNumberPagination чуть позже
    #permission_classes = чуть позже

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        #serializer.save(author=self.request.user, title=title)
        serializer.save(title=title) # Временно пока нет user модели


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    #pagination_class = PageNumberPagination чуть позже
    #permission_classes = чуть позже

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        #serializer.save(author=self.request.user, review=review)
        serializer.save(review=review)  # Временно пока нет user модели
