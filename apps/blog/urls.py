from django.urls import path
from .views import (
    api_home,
    # post_create,
    PostDetailView, PostCreateAPIView)


# app name
app_name = 'blog'

urlpatterns = [
    path('', api_home, name='blog-home'),
    # path('post-create/', post_create, name='post-create'),
    path('post-create/', PostCreateAPIView.as_view(), name='post-create'),
    path('post-detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
