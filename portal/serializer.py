from rest_framework import serializers
from portal.models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class getArticlesByCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"

class getArticlesByIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"





