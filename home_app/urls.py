from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home_app_home'),
    path('about/', views.about, name='app_about'),
]