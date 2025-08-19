from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.contrib.auth.urls import views as auth_views
from . import views
from home.views import register

# Define URL patterns for the application, mapping URLs to specific views
urlpatterns = [
    path('terminal-members/', views.terminal_members, name='terminal_members'),
    path('terminal-login/', views.terminal_login, name='terminal_login'),
    path('get/<str:name>/', views.get_member_info, name='get_member_info'),
    path('<str:year>/', views.team, name='team_by_year'),
    path('', views.team, name='team'),
]
