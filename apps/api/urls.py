from django.urls import path
from apps.blog.views import (
    api_home,
    create_post
)
app_name = 'api'

# all path for all api view here
urlpatterns = [
    path('', api_home, name='home'),
    path('create-post/', create_post, name='create-post'),
]
