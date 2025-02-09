from rest_framework import serializers
from .models import Poketype, Pokemon, Pokecard

class PokeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poketype
        fields = ["name", "url"]

class PokemonSerializer(serializers.ModelSerializer):
    type = PokeTypeSerializer(many=True, read_only=True)
    type_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Poketype.objects.all(), write_only=True) 

    class Meta:
        model = Pokemon
        fields = ["poke_id", "name", "order", "base_experience", 
        "is_shiny", "stats", "type", "type_ids"]

    def create(self, validated_data):
        type_ids = validated_data.pop('type_ids', [])
        pokemon = Pokemon.objects.create(**validated_data)
        pokemon.type.set(type_ids)
        return pokemon

class PokeCardSerializer(serializers.ModelSerializer):
    pokemon = PokemonSerializer()

    class Meta:
        model = Pokecard
        fields = ['owner', 'pokemon', 'rarity', 'border_style']

    def create(self, validated_data):
        pokemon_data = validated_data.pop('pokemon') # Pop the nested pokemon data
        pokemon = PokemonSerializer.create(PokemonSerializer(), validated_data=pokemon_data) # Create or update Pokemon
        pokecard = Pokecard.objects.create(pokemon=pokemon, **validated_data) # Create Pokecard
        return pokecard