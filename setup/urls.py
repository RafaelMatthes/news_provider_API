from django.contrib import admin
from django.urls import path, include, re_path
from portal.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('admin/articles', ArticleViewSet, basename='Articles')
router.register('admin/authors', AuthorViewSet, basename='Authors')
router.register('login', LoginViewSet, basename='Login')
router.register('sign-up', UserViewSet, basename='Signup')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path('^api/articles/(?P<category>.+)/$',  getArticlesByCategoryViewSet.as_view()),
    path('api/articles/<int:id>', getArticlesByIdViewSet.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
