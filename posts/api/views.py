from rest_framework import viewsets
from posts.models import Post, Comment
from posts.api.serializers import PostSerializer, CommentSerializer

class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer