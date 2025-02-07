from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from accounts.models import CustomUser

import requests
import json

class pokeView(APIView):

    def get(self, request, format=None):
        r = requests.get('https://pokeapi.co/api/v2/pokemon/35/')
        data = r.json()
        json_str = json.dumps(data, indent=4)

        json_object = json.loads(json_str)
        print(json_object['id'])
        print(json_object['name'])
        print(json_object['order'])
        print(json_object['base_experience'])
        print(json_object['stats'])
        print(json_object['types'])

        return Response('Hi')
