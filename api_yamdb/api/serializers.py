from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',
                  'slug', )
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',
                  'slug', )
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('category',
                  'genre',
                  'name',
                  'year',
                  'description', )
        model = Title


class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ('id',
                  'text',
                  'author'
                  'score',
                  'pub_date', )
        read_only_fields = ('title',)


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id',
                  'text',
                  'author'
                  'pub_date', )
        read_only_fields = ('review', )

