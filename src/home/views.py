from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from accounts.models import CustomUser
from home.models import Pokemon, Poketype, Pokecard
from home.serializers import PokemonSerializer, PokeTypeSerializer, PokeCardSerializer

import requests
import json
import random

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

class pokeView(APIView):
    def get(self, request, format=None):
        pass

def get_pokemon():
    poke_id = random.randint(1, 1000)
    POKEAPI_URL = f"{POKEAPI_BASE_URL}{poke_id}/"

    r = requests.get(POKEAPI_URL)
    data = r.json()
    return data

class ListPokecardView(ListAPIView):
    queryset = Pokecard.objects.all()
    serializer_class = PokeCardSerializer

class PokecardDetailView(RetrieveAPIView):
    queryset = Pokecard.objects.all()
    serializer_class = PokeCardSerializer

class CreatePokecardView(CreateAPIView):
    model = Pokecard
    serializer_class = PokeCardSerializer

    def create(self, request, *args, **kwargs):
        data = get_pokemon()

        # Transform the API data to match the serializer's expected format
        serializer_data = {
            "owner": request.user.id,
            "pokemon": { # Nested Pokemon data
                "poke_id": data['id'],
                "name": data['name'],
                "order": data['order'],
                "base_experience": data['base_experience'],
                "is_shiny": False,
                "stats": data['stats'],
                "type_ids": [],
            },
            "rarity": 'common',  # Get rarity from request data
            "border_style": 'basic', # Get border style from request data
        }

        for type_data in data['types']:
            name = type_data['type']['name']
            url = type_data['type']['url']
            poketype = Poketype.objects.filter(name__iexact=name).first()
            if poketype:
                serializer_data['pokemon']['type_ids'].append(poketype.id)
            else:
                poketype_serializer = PokeTypeSerializer(data={"name": name, "url": url})
                if poketype_serializer.is_valid():
                    poketype = poketype_serializer.save()
                    serializer_data['pokemon']['type_ids'].append(poketype.id)
                else:
                    print(poketype_serializer.errors)
                    
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

