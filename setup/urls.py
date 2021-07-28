from django.contrib import admin
from django.urls import path, include, re_path
from portal.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="News Provider API",
      default_version='v1',
      description="Just a simple news provider API.",
      contact=openapi.Contact(email="rafael.matthes@live.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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
    path('api/docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
