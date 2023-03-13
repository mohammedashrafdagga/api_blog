from django.urls import path

from .views import (
    LoginAPIView, LogoutAPIView,
    RegisterCreateAPIView
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'auth'
urlpatterns = [
    path('login-v2/', LoginAPIView.as_view(), name='login-v2'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('register/', RegisterCreateAPIView.as_view(), name='register')

]
