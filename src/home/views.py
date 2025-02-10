from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from accounts.models import CustomUser
from home.models import Pokemon, Poketype, Pokecard
from home.serializers import PokemonSerializer, PokeTypeSerializer, PokeCardSerializer

import requests, random, json

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

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

        is_shiny = random.random() < 0.029 #shiny chance (2.9%)

        # Random Rarity and Border Style
        rarity_choices = [choice[0] for choice in Pokecard.RarityChoices.choices]
        rarity = random.choice(rarity_choices)

        border_style_choices = [choice[0] for choice in Pokecard.BorderStyleChoices.choices]
        border_style = random.choice(border_style_choices)

        # Transform the API data to match the serializer's expected format
        serializer_data = {
            "owner": request.user.id,
            "pokemon": {
                "poke_id": data['id'],
                "name": data['name'],
                "order": data['order'],
                "base_experience": data['base_experience'],
                "stats": data['stats'],
                "type_ids": [],
            },
            "is_shiny": is_shiny,
            "rarity": rarity,
            "border_style": border_style,
        }

        for type_data in data["types"]:
            name = type_data["type"]["name"]
            url = type_data["type"]["url"]
            poketype, _ = Poketype.objects.get_or_create(name__iexact=name, defaults={"name": name, "url": url})
            serializer_data['pokemon']["type_ids"].append(poketype.id)
                    
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DestroyPokecardView(DestroyAPIView):
    queryset = Pokecard.objects.all()
    serializer_class = PokeCardSerializer
