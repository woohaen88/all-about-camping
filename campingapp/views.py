from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from campingapp.forms import CampingCreateForm
from campingapp.models import Camping
from utils.decorators import campingOwnerShipRequired

User = get_user_model()

has_ownership = [
    login_required,
    campingOwnerShipRequired,
]


# @method_decorator(login_required, "get")
# @method_decorator(login_required, "post")
class CampingCreateView(LoginRequiredMixin, CreateView):
    form_class = CampingCreateForm
    model = Camping
    template_name = "campingapp/create.html"
    context_object_name = "create_camping"
    success_url = reverse_lazy("campingapp:index")

    def form_valid(self, form):
        valid = super().form_valid(form)
        camping = form.save(commit=False)
        camping.user = self.request.user
        camping.save()
        return valid


# @method_decorator(login_required, "get")
# @method_decorator(login_required, "post")
class CampingDetailView(LoginRequiredMixin, DetailView):
    model = Camping
    template_name = "campingapp/detail.html"
    context_object_name = "detail_camping"

    def get_object(self, queryset=None):
        object = get_object_or_404(self.model, pk=self.kwargs.get("camping_pk"))
        return object


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class CampingUpdateView(UpdateView):
    model = Camping
    template_name = "campingapp/update.html"
    context_object_name = "update_camping"
    fields = (
        "name",
        "content",
        "image",
        "visited_dt",
    )

    # form_class = CampingCreateForm

    def get_object(self, queryset=None):
        obj = self.model.objects.get(pk=self.kwargs.get("camping_pk"))
        return obj


class CampingListView(ListView):
    model = Camping
    template_name = "campingapp/index.html"
    context_object_name = "camping_list"


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class CampingDeleteView(DeleteView):
    model = Camping
    template_name = "campingapp/delete.html"
    context_object_name = "target_camping"
    success_url = reverse_lazy("campingapp:index")

    def get_object(self, queryset=None):
        camping_pk = self.kwargs.get("camping_pk")
        queryset = get_object_or_404(self.model, pk=camping_pk)
        return queryset
