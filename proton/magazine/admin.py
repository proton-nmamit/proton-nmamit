from django.contrib import admin
from .models import Magazine

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'published_date', 'is_active', 'download_count']
    list_filter = ['is_active', 'year', 'published_date']
    search_fields = ['title', 'description', 'year']
    readonly_fields = ['download_count']
    
    fieldsets = (
        ('Magazine Information', {
            'fields': ('title', 'year', 'description')
        }),
        ('Files and Links', {
            'fields': ('drive_link', 'pdf_file', 'cover_image')
        }),
        ('Status', {
            'fields': ('is_active', 'published_date', 'download_count')
        }),
    )
