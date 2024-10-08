from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.get_items, name='item-list'),
    path('items/create/', views.create_item, name='item-create'),
    path('items/<int:id>/', views.get_item, name='item-detail'),
    path('items/<int:id>/update/', views.update_item, name='item-update'),
    path('items/<int:id>/delete/', views.delete_item, name='item-delete')    
]
