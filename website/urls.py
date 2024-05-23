from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('contacts/', views.contacts, name='contacts'),
    path('gratuip/', views.gratuip, name='gratuip'),
    path('<id>/', views.services_detail, name='services_detail'),
]