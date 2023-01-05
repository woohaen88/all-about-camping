from django.contrib import admin
from django.urls import path, include
from aboutCamping import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("accountapp.urls")),
    path("camping/", include("campingapp.urls")),
    path("", views.IndexView.as_view(), name="index"),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
