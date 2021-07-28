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
        fields = ['id', 'author', 'category', 'title', 'summary', 'firstParagraph', 'body']

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = AuthorSerializer(instance.author).data
        return response

class getArticlesByCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = AuthorSerializer(instance.author).data
        return response

class getArticlesByIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary', 'firstParagraph', 'body']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = AuthorSerializer(instance.author).data
        return response

class getArticlesByIdAnonymousSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Article
        fields = fields = ['id', 'author', 'category', 'title', 'summary', 'firstParagraph']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = AuthorSerializer(instance.author).data
        return response

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





