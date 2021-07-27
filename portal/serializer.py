from rest_framework import serializers
from django.contrib.auth import get_user_model
from portal.models import *


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=True)
    # author_id = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name', write_only=True)

    class Meta:
        model = Article
        fields = ['id', 'category', 'title', 'summary', 'firstParagraph', 'body', 'author']

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

class getArticlesByCategorySerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name', write_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'author_id', 'category', 'title', 'summary' ]

class getArticlesByIdSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name', write_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'author_id', 'category', 'title', 'summary', 'firstParagraph', 'body']

class getArticlesByIdAnonymousSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name', write_only=True)
   
    class Meta:
        model = Article
        fields = fields = ['id', 'author', 'author_id', 'category', 'title', 'summary', 'firstParagraph']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'password',
            'email'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user





