# from django.db.models import query
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from portal.models import *
from portal.serializer import *

class AuthorViewSet(viewsets.ModelViewSet):
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer

class ArticleViewSet(viewsets.ModelViewSet):
   
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class getArticlesByCategoryViewSet(generics.ListAPIView):

    queryset = Article.objects.all()    
    serializer_class = getArticlesByCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'id')
    search_fields = ['@category', '=id']



