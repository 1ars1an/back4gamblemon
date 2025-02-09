from rest_framework import serializers
from .models import Poketype, Pokemon, Pokecard

class PokeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poketype
        fields = ["name", "url"]

class PokemonSerializer(serializers.ModelSerializer):
    type = PokeTypeSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = ["poke_id", "name", "order", "base_experience", 
        "is_shiny", "stats", "type"]

class PokeCardSerializer(serializers.ModelSerializer):
    pokemon = PokemonSerializer()

    class Meta:
        model = Pokecard
        fields = ['owner', 'pokemon', 'rarity', 'border_style']