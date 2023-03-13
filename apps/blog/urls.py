from django.urls import path

from .views import (
    # api_home,
    # post_create,
    PostDetailView,
    PostListCreateAPIView,
    PostUpdateView,
    PostDestroyView,
    # PostMixinsAPIView
    CommentCreateAPIView
)


# app name
app_name = 'blog'

urlpatterns = [

    path('posts/', PostListCreateAPIView.as_view(), name='post'),
    path('post-update/<slug:slug>/', PostUpdateView.as_view(), name='post-update'),
    path('post-delete/<slug:slug>/', PostDestroyView.as_view(), name='post-delete'),
    path('post-detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/add-comment/',
         CommentCreateAPIView.as_view(), name='post-comment-add')

]
