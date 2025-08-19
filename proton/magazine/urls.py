from django.urls import path
from . import views

app_name = 'magazine'

urlpatterns = [
    path('', views.magazine_detail, name='magazine_detail'),
    path('<int:pk>/', views.magazine_detail, name='magazine_detail_pk'),
    path('list/', views.magazine_list, name='magazine_list'),
    path('download/<int:pk>/', views.track_download, name='track_download'),
]
