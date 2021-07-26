# from django.db.models import query
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from portal.models import *
from portal.serializer import *

from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        return ObtainAuthToken().as_view()(request=request._request)

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


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(UserViewSet, self).get_permissions()


