from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('booking-info/', views.booking_info, name='booking_info'),
    path('packages/', views.packages_list, name='packages_list'),
    path('packages/add/', views.add_package, name='add_package'),
    path('packages/edit/<int:pk>/', views.edit_package, name='edit_package'),
    path('packages/delete/<int:pk>/', views.delete_package, name='delete_package'),
    path('packages/add-booking/<int:package_id>/', views.add_booking, name='add_booking'),
]
