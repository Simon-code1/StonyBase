from django.contrib import admin
from .models import Project, ProjectImage, ContactMessage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "featured", "created_at")
    list_filter = ("category", "featured")
    search_fields = ("title", "short_description", "full_description", "location")
    inlines = [ProjectImageInline]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone")
    readonly_fields = ("created_at",)