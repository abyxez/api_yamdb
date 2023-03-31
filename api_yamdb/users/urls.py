from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, get_jwt_token, signup, user_me

router = SimpleRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('signup/', signup),
    path('token/', get_jwt_token),
    path('me/', user_me),
    path('', include(router.urls))
]
