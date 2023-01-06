from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from campingapp.models import Camping


def accountOwnerShipRequired(func):
    def decorated(request, *args, **kwargs):
        User = get_user_model()
        user = get_object_or_404(User, pk=kwargs.get("pk"))
        return func(request, *args, **kwargs)

    return decorated


def campingOwnerShipRequired(func):
    def decorated(request, *args, **kwargs):
        camping = get_object_or_404(Camping, pk=kwargs.get("camping_pk"))
        if camping.user != request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
