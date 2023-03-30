from django.urls import path
from .views import signup, get_jwt_token

app_name = 'users'

urlpatterns = [
    path('v1/auth/signup/', signup),
    path('v1/auth/token/', get_jwt_token)
]
