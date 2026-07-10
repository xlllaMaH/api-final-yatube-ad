"""Настройка админ зоны в posts."""
from django.contrib import admin
from .models import Comment, Group, Post, Follow


class PostAdmin(admin.ModelAdmin):
    """Настройка отображения для Post."""

    list_display = (
        'text',
        'pub_date',
        'image',
        'author',
    )
    search_fields = ('group',)
    list_filter = ('pub_date', 'author')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    """Настройка отображения для Comment."""

    list_display = (
        'author',
        'post',
        'text',
        'created'
    )
    search_fields = ('post',)
    list_filter = ('author', 'created')
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    """Настройка отображения для Group."""

    list_display = (
        'title',
        'slug',
        'description'
    )
    search_fields = ('slug',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    """Настройка отображения для Follow."""

    list_display = (
        'user',
        'follow'
    )
    search_fields = ('user',)
    list_filter = ('user',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Follow, FollowAdmin)
