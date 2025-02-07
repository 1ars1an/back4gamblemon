from django.urls import path
from .views import pokeView  # Import your view

urlpatterns = [
    path('poke/', pokeView.as_view(), name='pokeconfig'),  # Register the view
]
