from django import forms
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class AccoutSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        user = User.objects.filter(email=email).first()

        if user is not None:
            raise forms.ValidationError("email중복입니당")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.clean_email()
        user.set_password(self.clean_password2())
        if commit:
            user.save()
        return user


class AccountSignInForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "이메일"}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "패스워드"}
        ),
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("password is wrong"))

        except get_user_model().DoesNotExist:
            self.add_error("email", forms.ValidationError("이메일이 존재하지않음"))
