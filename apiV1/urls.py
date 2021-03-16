from django.urls import path
from apiV1.views import (
    userRegistration_view
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = "apiV1"
urlpatterns = [
    path('account/', userRegistration_view.as_view(), name='register'),
    path('login', obtain_auth_token, name='login')
]
