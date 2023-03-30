from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet, ReviewViewSet, CommentViewSet

router = DefaultRouter()
router.register('genres', GenreViewSet, basename='genres')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')
router.register(r'review/(?P<title_id>\d+)/comments', CommentViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
]