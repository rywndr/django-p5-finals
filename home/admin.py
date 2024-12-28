from django.contrib import admin

from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    def registration_number_display(self, obj):
        return f"{obj.registration_number:04d}"

    registration_number_display.short_description = "Registration Number"

    list_display = (
        "registration_number_display",
        "nama",
        "email",
        "kategori",
        "created_at",
    )
    search_fields = ("registration_number", "nama", "email")
    list_filter = ("kategori", "warga_negara", "created_at")
    readonly_fields = ("registration_number", "created_at", "updated_at")

    # Exclude registration_number from the add form
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj is None:  # This is an add operation
            fields = [f for f in fields if f != "registration_number"]
        return fields

    def save_model(self, request, obj, form, change):
        if not change:  # This is an add operation
            # The registration_number will be set automatically in the model's save method
            pass
        super().save_model(request, obj, form, change)
