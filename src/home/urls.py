from django.urls import path
from .views import ListPokecardView, PokecardDetailView, CreatePokecardView, DestroyPokecardView

urlpatterns = [
    path('cards/', ListPokecardView.as_view(), name='list-pokemon'),
    path('cards/<int:pk>', PokecardDetailView.as_view(), name='list-pokemon'),
    path('cards/create/', CreatePokecardView.as_view(), name='create-card'),
    path('cards/destroy/<int:pk>', DestroyPokecardView.as_view(), name='destroy-card'),
]

