from django.db.models import query
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

    def get_query_set(self):
        queryset = Article.objects.filter(category__icontains=self.kwargs.get('category'))
        return queryset
    
    serializer_class = getArticlesByCategorySerializer


