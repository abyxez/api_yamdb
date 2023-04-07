from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, get_jwt_token, signup, user_me

router = SimpleRouter()
router.register('', UserViewSet, basename='users')

app_name = 'users'

urlpatterns = [
    path('v1/auth/signup/', signup),
    path('v1/auth/token/', get_jwt_token),
    path('v1/users/me/', user_me),
    path('v1/users/', include(router.urls))
]
