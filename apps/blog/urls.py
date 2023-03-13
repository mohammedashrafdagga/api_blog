from django.urls import path

from .views import (
    # api_home,
    # post_create,
    PostDetailView,
    PostListAPIView,
    PostCreateAPIView,
    PostUpdateView,
    PostDestroyView,

    CommentCreateAPIView,
    CommentDestroyAPIView
)


# app name
app_name = 'post'

urlpatterns = [

    path('posts/', PostListAPIView.as_view(), name='posts'),
    path('post-create/', PostCreateAPIView.as_view(), name='post-create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', PostDestroyView.as_view(), name='post-delete'),
    path('post/<slug:slug>/add-comment/',
         CommentCreateAPIView.as_view(), name='post-comment-add'),
    path('post/comment/<int:pk>/delete/',
         CommentDestroyAPIView.as_view(), name='post-comment-delete'),

]
