"""
URL configuration for proton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import necessary modules from Django framework
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.contrib.auth.urls import views as auth_views
from django.conf import settings



# Define URL patterns for the application
urlpatterns = [
    # URL pattern for the admin interface
    path('admin404/', admin.site.urls),
    
    # Include URL patterns from the 'home' app
    path('', include('home.urls')),

    path('profile/', include('user_profile.urls')),
    
    # Include URL patterns for user authentication (login, logout, etc.)
    # This is provided by Django's built-in auth system
    path('accounts/', include('django.contrib.auth.urls')), 

    path('contact/', include('contact.urls')),

    path('gallery/', include('gallery.urls')),  # Remove namespace='gallery'

    path('team/', include('team.urls')),
    
    path('magazine/', include('magazine.urls')),
    
    # Serve media files (e.g., images, videos) from the MEDIA_ROOT directory
    # This is only active when the application is running in debug mode
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)