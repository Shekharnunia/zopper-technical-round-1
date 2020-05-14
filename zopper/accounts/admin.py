from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    fieldsets = (
        (
            "User Profile",
            {
                "fields": (
                    "avatar",
                )
            },
        ),
    ) + AuthUserAdmin.fieldsets
