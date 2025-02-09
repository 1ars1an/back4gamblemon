from django.urls import path
from .views import ListPokecardView  # Import your view

urlpatterns = [
    path('poke/', ListPokecardView.as_view(), name='list-pokemon'),  # Register the view
]
