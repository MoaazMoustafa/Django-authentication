from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import signup, logout

app_name = "account=v1"
urlpatterns = [
    path('api/v1/signup', signup, name="signup"),
    path('api/v1/login', obtain_auth_token, name="login_token"),
    path('api/v1/logout', logout, name="logout"),
]
