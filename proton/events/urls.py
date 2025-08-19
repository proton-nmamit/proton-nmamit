# Import necessary modules from Django for URL routing and configuration
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.urls import views as auth_views
from . import views

# Define URL patterns for the application, mapping URLs to specific views
urlpatterns = [
    path('', views.events, name='events'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
]
