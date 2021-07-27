# from django.db.models import query
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from portal.models import *
from portal.serializer import *

from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        return ObtainAuthToken().as_view()(request=request._request)

class AuthorViewSet(viewsets.ModelViewSet):
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer
        permissions_class = [IsAuthenticated]

class ArticleViewSet(viewsets.ModelViewSet):
   
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class getArticlesByCategoryViewSet(generics.ListAPIView):

    def get_queryset(self):

        aux = self.kwargs['category'].replace('-',' ')
        queryset = Article.objects.filter(category=aux)    
        
        return  queryset

    serializer_class = getArticlesByCategorySerializer
    
class getArticlesByIdViewSet(generics.ListAPIView):

    def get_queryset(self):

        queryset = Article.objects.filter(pk=self.kwargs['id'])    
        
        return queryset

    def get_serializer_class(self):

        user = self.request.user
        print('------', user)
        print(' --------- ',user.is_authenticated)
        if user.is_authenticated:    
            return getArticlesByIdSerializer
        else:
            return getArticlesByIdAnonymousSerializer

    serializer_class = get_serializer_class


    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('slug_category',)
    # search_fields = ['@slug_category',]

class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(UserViewSet, self).get_permissions()


