from rest_framework import viewsets
from albums.models import Album, Photo
from albums.api.serializers import AlbumSerializer, PhotoSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
