from django.urls import path
from .views import signup, get_jwt_token
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('v1/auth/signup/', signup),
    path('v1/auth/token/', get_jwt_token)
]
