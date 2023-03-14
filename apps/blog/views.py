from .models import Post
from rest_framework import generics,  permissions, status
from rest_framework.response import Response
from apps.api.permissions import IsOwner
from apps.api.mixins import PostMixinsSerializer, CommentMixinsSerializer
from apps.api.utils import get_post, get_user_token


class PostListAPIView(
        PostMixinsSerializer,
        generics.ListAPIView):
    # override the permission class
    permission_classes = [permissions.AllowAny]


class PostCreateAPIView(
        PostMixinsSerializer,
        generics.CreateAPIView):

    # override perform create
    def perform_create(self, serializer):
        serializer.save(author=get_user_token(self.request))
        return Response(status=status.HTTP_201_CREATED)


class PostDetailView(
        PostMixinsSerializer,
        generics.RetrieveAPIView):

    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]


class PostUpdateView(
        PostMixinsSerializer,
        generics.UpdateAPIView):

    lookup_field = 'slug'
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner
    ]


# Destroy
class PostDestroyView(
        PostMixinsSerializer,
        generics.DestroyAPIView):

    lookup_field = 'slug'
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner
    ]


# for creating comment into post
class CommentCreateAPIView(
        CommentMixinsSerializer,
        generics.CreateAPIView):

    def perform_create(self, serializer):
        serializer.save(author=get_user_token(
            self.request), post=get_post(self.kwargs.get('slug')))
        return Response(status=status.HTTP_201_CREATED)


class CommentDestroyAPIView(
        CommentMixinsSerializer,
        generics.DestroyAPIView):

    permission_classes = [
        permissions.IsAuthenticated,
        # Comment ALlow the Owner the Comment delete only
        IsOwner
    ]
    lookup_field = 'pk'
