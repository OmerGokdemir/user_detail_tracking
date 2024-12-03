from rest_framework.routers import DefaultRouter
from albums.api import views

router = DefaultRouter()

router.register(r'album', views.AlbumViewSet, basename='album')
router.register(r'photo', views.PhotoViewSet, basename='photo')

urlpatterns = router.urls