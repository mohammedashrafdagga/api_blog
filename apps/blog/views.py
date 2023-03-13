from .models import Post
from .serializers import PostSerializers, CommentSerializer
from rest_framework import generics,  permissions, authentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class PostDetailView(generics.RetrieveAPIView):
    '''
        Post Detail View
        - to retrieve single item in Post Model item
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    # permissions and authentication
    permission_classes = [
        # That mean can read only if not authentication or Authentication to post thing
        permissions.IsAuthenticatedOrReadOnly
    ]
    authentication_classes = [

        authentication.TokenAuthentication,
    ]


class PostListCreateAPIView(generics.ListCreateAPIView):
    '''
        Post List & Create API View
        - to create new instance from post and get all item in post model
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    authentication_classes = [

        authentication.TokenAuthentication,
    ]


class PostUpdateView(generics.UpdateAPIView):
    '''
        Post Update View
        - to Update single item in Post Model item by using slug
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    authentication_classes = [

        authentication.TokenAuthentication,
    ]


# Destroy
class PostDestroyView(generics.DestroyAPIView):
    '''
        Post Destroy View
        - to delete single item in Post Model item by using slug item
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
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
        post_slug = self.request.data.get('post_slug')
        return get_object_or_404(Post, slug=post_slug)

    def get_author(self):
        token = self.request.headers.get('Authorization').split(' ')[1]
        return get_object_or_404(Token, key=token).user

    # override the token
    def perform_create(self, serializer):
        serializer.save(author=self.get_author(), post=self.get_post())
        return Response(status=status.HTTP_201_CREATED)
