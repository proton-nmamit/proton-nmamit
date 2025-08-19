# Import necessary modules from Django for URL routing and configuration
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.contrib.auth.urls import views as auth_views
from . import views
from home.views import register
from django_user_agents.utils import get_user_agent
from .views import custom_404_view

# Define URL patterns for the application, mapping URLs to specific views
urlpatterns = [
    # Define the URL pattern for the home page, mapping to the 'index' view
    path('', views.index, name='home'),
    path('gallery/', include('gallery.urls')),
    path('team/', include('team.urls')),
    path('events/', include('events.urls')),
    path('terminal/', views.terminal, name='terminal'),
    #gui home
    # path("home/", views.home, name="gui-home"),
    path('terminal/home/', views.home, name='home'),
    path('home/', views.home, name='home'),
 
    # Define the URL pattern for user registration, mapping to the 'register' view
    path("register/", register, name="register"), 
    path("about/", views.about, name="about"),
    path('terminal_login/', views.terminal_login, name='terminal_login'),  # Updated path
    
]

handler404 = custom_404_view