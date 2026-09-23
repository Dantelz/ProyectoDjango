from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("styles.css", serve, {"path": "styles.css", "document_root": settings.BASE_DIR}),
    path("assets/<path:path>", serve, {"document_root": settings.BASE_DIR / "assets"}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
