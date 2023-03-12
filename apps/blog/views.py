from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializers
from rest_framework import generics


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Post.objects.all()
    data = {}
    if instance:
        data = PostSerializers(instance, many=True).data
    return Response(data)


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


class PostCreateAPIView(generics.CreateAPIView):
    '''
        Post Create API View
        - to create new instance from post
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def perform_create(self, serializer):

        # or get token send from serializer
        # token = serializer.validated_data['token']
        # user = Token.objects.get(token =token)
        # serializer.save(user = user)
        return super().perform_create(serializer)
