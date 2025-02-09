from django.urls import path
from .views import ListPokecardView, PokecardDetailView, CreatePokecardView, pokeView  # Import your view

urlpatterns = [
    path('cards/', ListPokecardView.as_view(), name='list-pokemon'),
    path('cards/<int:pk>', PokecardDetailView.as_view(), name='list-pokemon'),
    path('cards/create/', CreatePokecardView.as_view(), name='create-card'),
    path('poke/test', pokeView.as_view()),
]

