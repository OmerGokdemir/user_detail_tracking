from rest_framework import serializers
from albums.models import Album, Photo

base_url = "http://127.0.0.1:8000/media/"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
        
        
class PhotoSerializer(serializers.ModelSerializer):
    thumbnailUrl = serializers.SerializerMethodField()
    
    class Meta:
        model = Photo
        fields = ["id", "title", "url", "thumbnailUrl", "albumId"]
        
    def get_thumbnailUrl(self, obj):
        thumbnailUrl = base_url + str(obj.url)
        return thumbnailUrl