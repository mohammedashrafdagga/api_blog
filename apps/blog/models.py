from django.db import models
import uuid
from django.contrib.auth import get_user_model


# User Model
User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=2500)
    slug = models.SlugField(default=uuid.uuid4, unique=True)
    content = models.TextField()  # required field
    image = models.ImageField(
        upload_to='static/images/', blank=True, null=True)

    # create and update date
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # str method
    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()  # required
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:255]
