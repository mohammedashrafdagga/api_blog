from rest_framework import serializers
from .models import Post, Comment


# Comment the showing in Post Serializer
class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
            'create_at'
        ]


class PostSerializers(serializers.ModelSerializer):
    # slug = serializers.SerializerMethodField(read_only=True)
    comments = CommentPostSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'comments',

        ]


# another Comment Serializer to Save Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
