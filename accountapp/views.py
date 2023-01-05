from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from django.shortcuts import get_object_or_404

from accountapp.forms import AccountSignInForm, AccoutSignUpForm

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
