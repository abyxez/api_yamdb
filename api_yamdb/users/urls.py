from django.urls import path
from .views import signup
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('v1/auth/signup/', signup),
    # path('v1/auth/token/', TokenObtainPairWithoutPasswordView.as_view())
]
