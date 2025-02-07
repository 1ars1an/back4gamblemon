from rest_framework import serializers
from .models import PokeType, Pokemon, pokeCard

class PokeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokeType
        fields = ["id", "name", "url"]

