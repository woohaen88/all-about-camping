from django.db import models
from django.urls import reverse
from django.conf import settings


class Camping(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    visited_dt = models.DateTimeField()
    name = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="camping/%Y/%m/%d", blank=True)

    # ForeignKey
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="camping",
        null=True,
    )

    class Meta:
        verbose_name_plural = "camping"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("campingapp:detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("campingapp:update", args=(self.pk,))

    def get_delete_url(self):
        return reverse("campingapp:delete", args=(self.pk,))
