from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from accounts.models import CustomUser
from home.models import Pokemon, Poketype, Pokecard
from home.serializers import PokemonSerializer, PokeTypeSerializer, PokeCardSerializer

import requests
import json

# class pokeView(APIView):

#     def get(self, request, format=None):
#         r = requests.get('https://pokeapi.co/api/v2/pokemon/50/')
#         data = r.json()
#         json_str = json.dumps(data, indent=4)

#         json_object = json.loads(json_str)
#         print(json_object['id'])
#         print(json_object['name'])
#         print(json_object['order'])
#         print(json_object['base_experience'])
#         print(json.dumps(json_object['stats'], indent=2))
#         print(json_object['types'])

#         return Response('Hi')

class ListPokecardView(ListAPIView):
    queryset = Pokecard.objects.all()
    serializer_class = PokeCardSerializer

