from django.contrib import admin
from .models import Organization, Location


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_number', 'website', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'contact_number', 'website')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ("Organization Details", {
            'fields': ('name', 'email', 'contact_number', 'website')
        }),
        ("Status and Timestamps", {
            'fields': ('created_at', 'updated_at'),
        }),
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'organization', 'city', 'state', 'country', 'contact_number', 'created_at')
    list_filter = ('organization', 'city', 'state', 'country')
    search_fields = ('name', 'organization__name', 'city', 'state', 'country')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ("Location Details", {
            'fields': ('organization', 'name', 'address', 'city', 'state', 'country', 'postal_code')
        }),
        ("Contact Info", {
            'fields': ('contact_number', 'email', 'website'),
        }),
        ("Status and Timestamps", {
            'fields': ('created_at', 'updated_at'),
        }),
    )
