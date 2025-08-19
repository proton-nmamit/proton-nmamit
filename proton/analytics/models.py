from django.db import models
from django.contrib.auth.models import User

class UserEvent(models.Model):
    EVENT_CHOICES = (
        ('page_view', 'Page View'),
        ('site_visit', 'Site Visit'),
    )

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    page_url = models.URLField(max_length=2000)
    page_name = models.CharField(max_length=255, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    device_type = models.CharField(max_length=50, blank=True)
    browser = models.CharField(max_length=100, blank=True)
    operating_system = models.CharField(max_length=100, blank=True)
    referrer = models.URLField(max_length=2000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.user or 'Anonymous'} - {self.event_type} on {self.page_name or self.page_url} at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'User Event'
        verbose_name_plural = 'User Events'
