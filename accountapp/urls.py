from django.urls import path
from accountapp import views

app_name = "accountapp"
urlpatterns = [
    path("signup/", views.AccountSignUpView.as_view(), name="signup"),
    path("login/", views.AccountLoginView.as_view(), name="login"),
    path("update/<int:update_pk>/", views.AccountUpdateView.as_view(), name="update"),
    path("logout/<int:logout_pk>/", views.AccountLogoutView.as_view(), name="logout"),
]
