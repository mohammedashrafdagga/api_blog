from rest_framework import serializers
from .models import Post, Comment


# another Comment Serializer to Save Comment
class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'create_at']


class PostSerializers(serializers.ModelSerializer):
    post_comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'post_comments'
        ]

    def get_post_comments(self, obj):
        comments = Comment.objects.filter(post=obj)
        data = CommentPostSerializer(comments, many=True).data
        return data


# another Comment Serializer to Save Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
