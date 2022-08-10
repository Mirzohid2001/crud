from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome),
    path('load_form/', load_form),
    path('add/', add, name = 'add'),
    path('show/', show),
    path('edit/<int:pk>', edit, name='edit'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
    path('search/', search)
    
] 