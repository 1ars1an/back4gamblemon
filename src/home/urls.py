from django.urls import path
from .views import ListPokecardView, CreatePokecardView, PokecardRetrieveUpdateDeleteView

urlpatterns = [
    path('cards/', ListPokecardView.as_view(), name='list-pokemon'),
    path('cards/<int:pk>', PokecardRetrieveUpdateDeleteView.as_view(), name='getdelupdate-pokemon'),
    path('cards/create/', CreatePokecardView.as_view(), name='create-card'),
]

