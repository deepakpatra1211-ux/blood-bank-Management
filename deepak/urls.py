from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stock/', views.stock, name='stock'),
    path('apply/', views.apply, name='apply'),
    path('location/', views.location, name='location'),
]
