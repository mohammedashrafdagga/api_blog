from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from django.forms.models import model_to_dict
from .serializers import BLogSerializers


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Blog.objects.all()
    data = {}
    if instance:
        data = BLogSerializers(instance, many=True).data
    return Response(data)
