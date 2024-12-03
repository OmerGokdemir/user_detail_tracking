from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from user_detail_tracking import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.api.urls")),
    path("posts/", include("posts.api.urls")),
    path("albums/", include("albums.api.urls")),
    path("todos/", include("todos.api.urls")),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)