from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='Tienda'),
    path('cart/', views.cart, name='Carrito'),
    path('checkout/', views.checkout, name='Pago'),
    path('update_item/', views.updateItem, name='update_item'),
]