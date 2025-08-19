# Import necessary modules from Django for URL routing and configuration
from django.urls import path
from . import views

# Define URL patterns for the application, mapping URLs to specific views
urlpatterns = [
    path('', views.photos, name='photos'),
]