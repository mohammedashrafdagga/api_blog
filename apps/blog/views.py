from .models import Post
from .serializers import PostSerializers, CommentSerializer
from rest_framework import generics,  permissions, authentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


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

    # override the token
    def perform_create(self, serializer):
        token_key = self.request.headers.get('Authorization').split(' ')[1]
        user = Token.objects.get(key=token_key).user
        post = Post.objects.get(slug=self.kwargs.get('post_id'))
        serializer.save(user=user, post=post)
        return Response(status=status.HTTP_201_CREATED)
