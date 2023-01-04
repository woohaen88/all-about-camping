from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accountapp.forms import AccountSignUpForm, AccountUpdateForm


class AccountSignUpView(CreateView):
    model = get_user_model()
    form_class = AccountSignUpForm
    template_name = "accountapp/signup.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class AccountLoginView(LoginView):
    template_name = "accountapp/login.html"


class AccountUpdateView(UpdateView):
    model = get_user_model()
    form_class = AccountUpdateForm
    template_name = "accountapp/update.html"


class AccountLogoutView(LogoutView):
    template_name = "accountapp/logout.html"
