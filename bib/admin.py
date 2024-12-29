from django.contrib import admin

from .models import Bib


@admin.register(Bib)
class BibAdmin(admin.ModelAdmin):
    list_display = ("bib", "created_at")
    search_fields = ("bib",)
    readonly_fields = ("created_at", "updated_at")
