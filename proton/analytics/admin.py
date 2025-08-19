from django.contrib import admin
from .models import UserEvent

@admin.register(UserEvent)
class UserEventAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'event_type', 'page_name', 'device_type', 'browser', 'operating_system', 'ip_address')
    list_filter = ('event_type', 'device_type', 'browser', 'operating_system', 'timestamp')
    search_fields = ('user__username', 'page_url', 'page_name', 'ip_address', 'user_agent')
    readonly_fields = ('timestamp', 'user', 'session_key', 'event_type', 'page_url', 'page_name', 'ip_address', 'user_agent', 'device_type', 'browser', 'operating_system', 'referrer', 'additional_data')
    date_hierarchy = 'timestamp'
    list_per_page = 25

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
