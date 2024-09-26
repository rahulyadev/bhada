from django.contrib import admin
from owner.models import Owner


class OwnerModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "upi_id",
    )
    search_fields = (
        "user",
        "upi_id",
    )
    ordering = (
        "user",
        "upi_id",
    )


admin.site.register(Owner, OwnerModelAdmin)
