from rest_framework import serializers
from .models import Post, Comment

# another Comment Serializer to Save Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='post:post-comment-delete',
        read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'create_at', 'delete_url']


class PostSerializers(serializers.HyperlinkedModelSerializer):

    author = serializers.CharField(read_only=True)  # just read only
    # get all comment related the post
    post_comments = serializers.SerializerMethodField(read_only=True)
    # add comment
    add_comment_url = serializers.HyperlinkedIdentityField(
        view_name='post:post-comment-add',
        lookup_field='slug',
        read_only=True

    )
    # for user
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='post:post-detail',
        lookup_field='slug',
        read_only=True

    )

    edit_url = serializers.HyperlinkedIdentityField(
        view_name='post:post-update',
        lookup_field='slug',
        read_only=True
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='post:post-delete',
        lookup_field='slug',
        read_only=True
    )

    # comment

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'content',
            'add_comment_url',
            'detail_url',
            'edit_url',
            'delete_url',
            'post_comments',
        ]

    def get_post_comments(self, obj):
        comments = Comment.objects.filter(post=obj)
        data = CommentSerializer(comments, many=True, context={
                                 'request': self.context['request']}).data
        return data
