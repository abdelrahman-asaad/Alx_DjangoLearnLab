from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    #to specify that author is readonly

    class Meta:
        model = Comment
        fields = ["id", "author", "content", "created_at", "updated_at"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)
    #to specify that author and comment is readonly

    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "created_at", "updated_at", "comments"]
