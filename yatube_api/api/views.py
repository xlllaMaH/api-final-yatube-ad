"""Views for api."""
from django.shortcuts import get_object_or_404
from rest_framework import (
    viewsets,
    filters,
    exceptions,
    permissions,
    status,
    mixins
)
from rest_framework.decorators import action
from rest_framework.response import Response
from posts.models import Post, Group, Follow, Comment

from .serializers import (
    PostSerializer,
    GroupSerializer,
    FollowSerializer,
    CommentSerializer
)
from .pagination import PostPagination
from .permissions import AuthorOrReadOnly, ReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, AuthorOrReadOnly
    ]
    pagination_class = PostPagination

    def perform_create(self, serializer):
        """Save object and assign author."""
        serializer.save(author=self.request.user)

    def get_permissions(self):
        """Choose permissions."""
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    @action(detail=True, methods=['GET', 'POST'], url_path='comments')
    def comment_list(self, request, pk=None):
        """Request processing."""
        post = self.get_object()
        if request.method == 'POST':
            serializer = CommentSerializer(
                data=request.data, context={'request': request}
            )
            if serializer.is_valid():
                serializer.save(author=request.user, post=post)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=['GET', 'PUT', 'PATCH', 'DELETE'],
        url_path=r'comments/(?P<comment_id>\d+)'
    )
    def comment_detail(self, request, pk=None, comment_id=None):
        """Request processing."""
        post = self.get_object()
        comment = get_object_or_404(Comment, id=comment_id, post=post)
        if request.method == 'GET':
            serializer = CommentSerializer(comment)
            return Response(serializer.data)

        if comment.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        elif request.method == 'PUT' or request.method == 'PATCH':
            serializer = CommentSerializer(
                comment, data=request.data, partial=request.method == 'PATCH'
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_200_OK
                )
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        elif request.method == 'DELETE':
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """ViewSet for Follow."""

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('^following__username',)

    def get_queryset(self):
        """Get queryset for certain user."""
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Save object and ban on self-subscription."""
        following_user = serializer.validated_data["following"]

        if self.request.user == following_user:
            raise exceptions.ValidationError(
                'Вы не можете подписаться на самого себя'
            )

        serializer.save(user=self.request.user)
