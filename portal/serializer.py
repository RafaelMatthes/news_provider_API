from rest_framework import serializers
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





