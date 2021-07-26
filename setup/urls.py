from django.contrib import admin
from django.urls import path, include
from portal.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()

router.register('admin/articles', ArticleViewSet, basename='Articles')
router.register('admin/authors', AuthorViewSet, basename='Authors')
# router.register('articles/<slug:category>', CategoryViewSet, basename='Articles')


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/articles/<slug:category>', getArticlesByCategoryViewSet.as_view()),
    path('api/articles/<int:id>', getArticlesByIdViewSet.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
