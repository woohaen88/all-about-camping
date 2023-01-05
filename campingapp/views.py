from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from campingapp.forms import CampingCreateForm
from campingapp.models import Camping

User = get_user_model()


class CampingCreateView(CreateView):
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


class CampingDetailView(DetailView):
    model = Camping
    template_name = "campingapp/detail.html"
    context_object_name = "detail_camping"

    def get_object(self, queryset=None):
        object = get_object_or_404(self.model, pk=self.kwargs.get("camping_pk"))
        return object


class CampingUpdateView(UpdateView):
    model = Camping
    template_name = "campingapp/update.html"
    context_object_name = "update_camping"
    form_class = CampingCreateForm

    def get_object(self, queryset=None):
        object = get_object_or_404(self.model, pk=self.kwargs.get("camping_pk"))
        return object

    def post(self, request, *args, **kwargs):
        self.form_class = self.form_class(
            request.POST, request.FILES, instance=self.object
        )
        return super().post(request, *args, **kwargs)


class CampingListView(ListView):
    model = Camping
    template_name = "campingapp/index.html"
    context_object_name = "camping_list"
