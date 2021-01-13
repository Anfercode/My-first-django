# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """
    Profile Admin
    """

    list_display = (
        "pk",
        "user",
        "title",
    )

    list_display_links = (
        "pk",
        "user",
        "title",
    )

    search_fields = (
        "pk",
        "title",
        'user__username',
    )

    list_filter = (
        'created_at',
        'updated_at',
    )

    readonly_fields = ('created_at', 'updated_at')