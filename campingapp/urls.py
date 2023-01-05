from django.urls import path
from campingapp import views

app_name = "campingapp"
urlpatterns = [
    # /camping/create/
    path("create/", views.CampingCreateView.as_view(), name="create"),
    # path("delete/<int:camping_pk>/", "view", name="delete"),
    path("detail/<int:camping_pk>/", views.CampingDetailView.as_view(), name="detail"),
    path("update/<int:camping_pk>/", views.CampingUpdateView.as_view(), name="update"),
    path("", views.CampingListView.as_view(), name="index"),
]
