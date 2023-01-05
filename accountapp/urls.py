from django.urls import path
from accountapp import views

app_name = "accountapp"

urlpatterns = [
    # account/signin
    path("signin/", views.AccountSignInView.as_view(), name="signin"),
    path("signup/", views.AccountSignUpView.as_view(), name="signup"),
]
