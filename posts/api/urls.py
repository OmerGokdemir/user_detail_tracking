from rest_framework.routers import DefaultRouter
from posts.api import views

router = DefaultRouter()

router.register(r"post", views.PostModelViewSet, basename="post")
router.register(r"comment", views.CommentModelViewSet, basename="comment")

urlpatterns = router.urls