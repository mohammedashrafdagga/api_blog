from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from django.forms.models import model_to_dict


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    blog_item = Blog.objects.all()
    data = {}
    if blog_item:
        data = model_to_dict(blog_item, fields=['title', 'content'])
    return Response(data, many=True)
