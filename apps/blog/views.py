from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializers


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Post.objects.all()
    data = {}
    if instance:
        data = PostSerializers(instance, many=True).data
    return Response(data)


@api_view(['POST'])
def create_post(request):
    serializer = PostSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response(serializer.data)

    # else
    return Response({'invalid': 'Data not correct'})
