from .models import Post, Comment
from .serializers import PostSerializers, CommentSerializer
from rest_framework import generics,  permissions, authentication, status
from rest_framework.response import Response
from .permissions import IsOwner
from .token import get_user_token
from django.shortcuts import get_object_or_404


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.AllowAny]


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=get_user_token(self.request))
        return Response(status=status.HTTP_201_CREATED)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [
        permissions.AllowAny
    ]


class PostUpdateView(generics.UpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner
    ]
    authentication_classes = [

        authentication.TokenAuthentication,
    ]


# Destroy
class PostDestroyView(generics.DestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner
    ]
    authentication_classes = [

        authentication.TokenAuthentication,
    ]


# for creating comment into post
class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_post(self):
        post_slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=post_slug)

    def perform_create(self, serializer):
        serializer.save(author=get_user_token(
            self.request), post=self.get_post())
        return Response(status=status.HTTP_201_CREATED)


class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        # Comment ALlow the Owner the Comment delete only
        IsOwner
    ]
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    lookup_field = 'pk'
