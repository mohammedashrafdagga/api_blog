from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

# Allow to get user from token


def get_user_token(request):
    token = request.headers.get('Authorization').split(' ')[1]
    return get_object_or_404(Token, key=token).user
