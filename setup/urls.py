from django.contrib import admin
from django.urls import path, include, re_path
from portal.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()

router.register('admin/articles', ArticleViewSet, basename='Articles')
router.register('admin/authors', AuthorViewSet, basename='Authors')


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/articles/', getArticlesByCategoryViewSet.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
