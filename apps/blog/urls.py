from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    # api_home,
    # post_create,
    PostDetailView,
    PostListCreateAPIView,
    PostUpdateView,
    PostDestroyView,
    # PostMixinsAPIView
)


# app name
app_name = 'blog'

urlpatterns = [
    path('auth/', obtain_auth_token, name='auth'),
    # path('', PostListAPIView.as_view(), name='blog-home'),
    # path('post-create/', post_create, name='post-create'),
    path('', PostListCreateAPIView.as_view(), name='post'),
    path('post-update/<slug:slug>/', PostUpdateView.as_view(), name='post-update'),
    path('post-delete/<slug:slug>/', PostDestroyView.as_view(), name='post-delete'),
    path('post-detail/<slug:slug>/',
         PostDetailView.as_view(), name='post-detail'),
    # update and destroy item in post model

]
