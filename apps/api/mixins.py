from apps.blog.serializers import PostSerializers, CommentSerializer
from apps.blog.serializers import Post, Comment


class PostMixinsSerializer():
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class CommentMixinsSerializer():
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
