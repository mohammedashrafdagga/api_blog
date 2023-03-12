from rest_framework import serializers
from .models import Blog


class BLogSerializers(serializers.ModelSerializer):
    # slug = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Blog
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
