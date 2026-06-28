from django.contrib import admin
from .models import Project
from .models import ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "featured", "created_at")
    list_filter = ("category", "featured")
    search_fields = ("title", "short_description", "full_description", "location")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone")
    readonly_fields = ("created_at",)