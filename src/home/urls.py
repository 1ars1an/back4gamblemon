from django.urls import path
from .views import ListPokecardView, pokeView  # Import your view

urlpatterns = [
    path('poke/', ListPokecardView.as_view(), name='list-pokemon'),
    path('poke/test', pokeView.as_view()),
]
