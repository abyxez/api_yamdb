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

    # author = serializers.SlugRelatedField(
    #     slug_field='username',
    #     read_only=True,
    #     default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ('id',
                  'text',
                  # 'author' пока без автора
                  'score',
                  'pub_date',)
        read_only_fields = ('title',)


class CommentSerializer(serializers.ModelSerializer):

    # author = serializers.SlugRelatedField(
    #     slug_field='username',
    #     read_only=True,
    #     default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id',
                  'text',
                  # 'author' пока без автора
                  'pub_date',)
        read_only_fields = ('title', 'review')

