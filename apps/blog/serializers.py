from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    # slug = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            # 'slug',
            'create_at',
            'update_at'
        ]

    # def get_slug(self, obj):
    #     return f'localhost:8000/api/{obj.slug}'
