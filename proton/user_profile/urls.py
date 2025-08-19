from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.contrib.auth.urls import views as auth_views
from . import views
from home.views import register
from .views import render

# Define URL patterns for the application, mapping URLs to specific views
urlpatterns = [
    path('', views.profile, name='profile'),
]