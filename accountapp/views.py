from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView
from django.shortcuts import get_object_or_404

from accountapp.forms import AccountSignInForm, AccoutSignUpForm, AccountUpdateForm

User = get_user_model()


class AccountSignInView(FormView):
    template_name = "accountapp/signin.html"
    form_class = AccountSignInForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        valid = super().form_valid(form)
        email = form.cleaned_data.get("email")
        user = get_user_model().objects.get(email=email)
        if user is not None:
            login(self.request, user)
        return valid


class AccountSignUpView(CreateView):
    template_name = "accountapp/signup.html"
    form_class = AccoutSignUpForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        valid = super().form_valid(form)
        email = form.cleaned_data.get("email")
        user = get_object_or_404(User, email=email)
        login(self.request, user)
        return valid


class AccountUpdateView(UpdateView):
    template_name = "accountapp/update.html"
    form_class = AccountUpdateForm
    context_object_name = "target_user"
    pk_url_kwarg = "account_pk"
    model = User

    def get_queryset(self):
        account_pk = self.kwargs.get("account_pk")
        return self.model.objects.filter(pk=account_pk)


class AccountSignOutView(LogoutView):
    template_name = "accountapp/signout.html"
