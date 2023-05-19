from django.urls import path
from .views import saludar

urlpatterns = [
    path('example/', saludar, name='saludar'),
    # Add more URL patterns here
]