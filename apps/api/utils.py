from django.shortcuts import get_object_or_404
from apps.blog.models import Post
from rest_framework.authtoken.models import Token


# get post objects
def get_post(post_slug):
    return get_object_or_404(Post, slug=post_slug)


# get user objects

def get_user_token(request):
    token = request.headers.get('Authorization').split(' ')[1]
    return get_object_or_404(Token, key=token).user
