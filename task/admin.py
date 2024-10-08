from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser

from .models import Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1
    fields = ("title", "status", "priority", "due_date", "category")
    readonly_fields = ("due_date",)
    show_change_link = True


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
    )
    search_fields = ("email", "first_name")
    ordering = ("-date_joined",)
    inlines = [TaskInline]

    fieldsets = (
        (None, {"fields": ("email", "profile_pix")}),
        ("Personal info", {"fields": ("first_name",)}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "password1", "password2"),
            },
        ),
    )


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "priority",
        "due_date",
        "category",
        "assigned_to",
    )
    list_filter = ("status", "priority", "category", "due_date")
    search_fields = ("title", "description", "category", "assigned_to__username")
    ordering = ("due_date",)
    fields = (
        "title",
        "description",
        "status",
        "priority",
        "due_date",
        "category",
        "assigned_to",
    )


admin.site.register(Task, TaskAdmin)
