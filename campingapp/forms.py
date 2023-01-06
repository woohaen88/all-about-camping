from django import forms
from campingapp.models import Camping


class CampingCreateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={"type": "file"}))
    visited_dt = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "date"}))

    class Meta:
        model = Camping
        fields = (
            "name",
            "content",
        )


class CampingUpdateForm(CampingCreateForm):
    pass
