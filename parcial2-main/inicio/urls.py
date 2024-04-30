from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.inicio, name='inicio'),
    path('new/', views.create_user, name='create_user'),
    path('register/', views.register, name='Registro'),
]