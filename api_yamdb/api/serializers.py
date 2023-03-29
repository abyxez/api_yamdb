from rest_framework import serializers

from titles.models import User, Category, Genre, Title, Review, Comment


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
    class Meta:
        fields = ('title_id',
                  'text',
                  'score', )
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title_id',
                  'review_id',
                  'text', )
        model = Comment
