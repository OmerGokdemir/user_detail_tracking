from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "userId"]
    list_display_links = ["title"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "postId"]
    list_display_links = ["name"]
