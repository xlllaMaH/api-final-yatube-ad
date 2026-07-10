"""Serializers for api."""
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        """Metadata for Post."""

        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment."""

    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """Metadata for Comment."""

        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group."""

    class Meta:
        """Metadata for Group."""

        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for Follow."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        """Metadata for Follow."""

        fields = ('user', 'following')
        model = Follow
