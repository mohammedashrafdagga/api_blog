from django.urls import path
from blog.views import api_home
app_name = 'api'

# all path for all api view here
urlpatterns = [
    path('', api_home, name='home'),
]