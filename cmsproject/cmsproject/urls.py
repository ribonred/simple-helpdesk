from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("section.urls")),
    path('notif/', include(notifications.urls), name='notifications'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)