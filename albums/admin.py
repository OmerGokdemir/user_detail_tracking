from django.contrib import admin
from .models import Album, Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "userId"]
    list_display_links = ["title"]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "albumId"]
    list_display_links = ["title"]