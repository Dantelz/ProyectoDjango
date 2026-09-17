from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "comment_count")
    list_display_links = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")
    ordering = ("-created_at",)

    @admin.display(description="comentarios")
    def comment_count(self, post):
        return post.comments.count()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author_name", "post", "created_at")
    list_filter = ("created_at",)
    search_fields = ("author_name", "author_email", "body")
    readonly_fields = ("created_at",)
