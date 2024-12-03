from rest_framework.routers import DefaultRouter
from todos.api import views

router = DefaultRouter()

router.register(r"todo", views.TodoModelViewSet, basename="todo")

urlpatterns = router.urls