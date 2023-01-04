from django.contrib import admin
from django.urls import path, include
from aboutCamping import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("accountapp.urls")),
    path("camping/", include("campingapp.urls")),
    path("", views.IndexView.as_view(), name="index"),
]
