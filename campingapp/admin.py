from django.contrib import admin
from campingapp.models import Camping


@admin.register(Camping)
class CampingAdmin(admin.ModelAdmin):
    pass
