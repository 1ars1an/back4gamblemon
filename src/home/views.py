from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from accounts.models import CustomUser
from home.models import Pokemon, Poketype, Pokecard
from home.serializers import PokemonSerializer, PokeTypeSerializer, PokeCardSerializer

import requests
import json
import random

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

class pokeView(APIView):

    def get(self, request, format=None):
        poke_id = random.randint(1, 1000)
        POKEAPI_URL = f"{POKEAPI_BASE_URL}{poke_id}/"

        r = requests.get(POKEAPI_URL)
        data = r.json()
        print(type(data))
        print(data['id'])
        print(data['name'])
        print(data['order'])
        print(data['base_experience'])
        print(json.dumps(data['stats'], indent=2))
        print(data['types'])
        return Response('Hi')


def get_pokemon():
    poke_id = random.randint(1, 1000)
    POKEAPI_URL = f"{POKEAPI_BASE_URL}{poke_id}/"

    r = requests.get(POKEAPI_URL)
    data = r.json()
    return data

class ListPokecardView(ListAPIView):
    queryset = Pokecard.objects.all()
    serializer_class = PokeCardSerializer

class CreatePokecardView(CreateAPIView):
    serializer_class = PokeCardSerializer

