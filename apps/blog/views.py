from .models import Post
from .serializers import PostSerializers
from rest_framework import generics, mixins, permissions, authentication


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

    def perform_destroy(self, instance):
        # just delete it.
        return super().perform_destroy(instance)


# Using Mixins API View
class PostMixinsAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    '''
        Using Mixins With Api View
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        if slug:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
