from .models import Post
from .serializers import PostSerializers
from rest_framework import generics, mixins


# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     instance = Post.objects.all()
#     data = {}
#     if instance:
#         data = PostSerializers(instance, many=True).data
#     return Response(data)


# @api_view(['POST'])
# def post_create(request):
#     serializer = PostSerializers(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         instance = serializer.save()
#         return Response(serializer.data)

#     # else
#     return Response({'invalid': 'Data not correct'})


class PostDetailView(generics.RetrieveAPIView):
    '''
        Post Detail View
        - to retrieve single item in Post Model item
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    # Post.objects.get(slug = slug)


# class PostCreateAPIView(generics.CreateAPIView):
#     '''
#         Post Create API View
#         - to create new instance from post
#     '''
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

#     def perform_create(self, serializer):

#         # or get token send from serializer
#         # token = serializer.validated_data['token']
#         # user = Token.objects.get(token =token)
#         # serializer.save(user = user)
#         return super().perform_create(serializer)


class PostListCreateAPIView(generics.ListCreateAPIView):
    '''
        Post List & Create API View
        - to create new instance from post and get all item in post model
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def perform_create(self, serializer):

        # or get token send from serializer
        # token = serializer.validated_data['token']
        # user = Token.objects.get(token =token)
        # serializer.save(user = user)
        return super().perform_create(serializer)

# Update and delete


class PostUpdateView(generics.UpdateAPIView):
    '''
        Post Update View
        - to Update single item in Post Model item by using slug
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'

    def perform_update(self, serializer):
        # not have anything to play with in here
        return super().perform_update(serializer)


# Destroy
class PostDestroyView(generics.DestroyAPIView):
    '''
        Post Destroy View
        - to delete single item in Post Model item by using slug item
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'

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
