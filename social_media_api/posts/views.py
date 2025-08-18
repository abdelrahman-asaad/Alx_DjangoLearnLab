from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class IsOwnerOrReadOnly(permissions.BasePermission): # creating custom permission
    def has_object_permission(self, request, view, obj): #built-in method for view permission in DRF
        # Allow read-only requests
        if request.method in permissions.SAFE_METHODS: #SAFE_METHODS = ["GET", "HEAD", "OPTIONS"] for read only
            return True
        # Only owner can edit/delete
        return obj.author == request.user #to ask if the user is the author ? and if true it returns
        #true, and if not it returns false
      


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer): #built-in method
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#Implement the Feed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def feed_view(request):
    # Get users the current user is following
    following_users = request.user.following.all()

    # Get posts from those users
    posts = Post.objects.filter(author__in=following_users).order_by("-created_at")

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)