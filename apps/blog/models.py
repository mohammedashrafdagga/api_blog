from django.db import models
import uuid


class Blog(models.Model):
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
