from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin


class UserModelAdmin(UserAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "is_admin",
        "is_staff",
        "is_owner",
        "is_tenant",
    )
    list_filter = ("is_admin", "is_owner", "is_tenant")
    fieldsets = (
        ("User Credentials", {"fields": ("phone_number", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_admin",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "password",
                ),
            },
        ),
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
        "phone_number",
    )
    ordering = (
        "email",
        "id",
        "phone_number",
    )
    filter_horizontal = ()


admin.site.register(User, UserModelAdmin)
