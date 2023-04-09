from django.shortcuts import get_object_or_404
from django_filters import CharFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import mixins, status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from reviews.models import Category, Genre, Review, Title

from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleCreateSerializer, TitleListSerializer)


def get_title_review_instance(self):
    if self.kwargs.get('review_id'):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review
    else:
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title


class CreateListDeleteViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class CategoryViewSet(CreateListDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)


class GenreViewSet(CreateListDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)


class TitleFilter(FilterSet):
    category = CharFilter(field_name='category__slug')
    genre = CharFilter(field_name='genre__slug')

    class Meta:
        model = Title
        fields = ('name', 'year', 'category', 'genre')


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)

    #def create(self, request):
    #    serializer = TitleCreateSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        serializer = TitleListSerializer(data=request.data)
    #        if serializer.is_valid():
    #            return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TitleListSerializer
        return TitleCreateSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,
                          )

    def get_queryset(self):
        title = get_title_review_instance(self)
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_title_review_instance(self)
        serializer.save(author=self.request.user, title=title)

    def create(self, request, title_id=None):
        if Review.objects.filter(
                title=self.kwargs.get('title_id'),
                author=request.user
        ).exists():
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, title_id)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,
                          )

    def get_queryset(self):
        review = get_title_review_instance(self)
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_title_review_instance(self)
        serializer.save(author=self.request.user, review=review)
