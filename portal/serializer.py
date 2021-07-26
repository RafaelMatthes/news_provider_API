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
        fields = "__all__"

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

class getArticlesByCategorySerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name', write_only=True)

    class Meta:
        model = Article
        fields = "__all__"

class getArticlesByIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"

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





