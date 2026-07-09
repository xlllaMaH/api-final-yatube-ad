from rest_framework import viewsets, filters, exceptions
from posts.models import Post, Group, Follow

from .serializers import PostSerializer, GroupSerializer, FollowSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        following_user = serializer.validated_data["following"]

        if self.request.user == following_user:
            raise exceptions.ValidationError(
                'Вы не можете подписаться на самого себя'
            )

        serializer.save(user=self.request.user)
