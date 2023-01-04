from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class AccountSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountUpdateForm, self).__init__(*args, **kwargs)
        self.fields["username"].disabled = True
